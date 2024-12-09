import os
import fitz
from nltk.tokenize import sent_tokenize
import logging
import ray


# 로그 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


@ray.remote
class DataParsing:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)  # Ensure output directory exists

    def pdf_search(self):
        """Returns a list of PDF files in the input directory."""
        return [f for f in os.listdir(self.input_dir)]

    def pdf_parsing(self):
        """Processes the PDF files and extracts text."""
        pdf_files = self.pdf_search()  # 클래스 내부 메서드 호출
        if not pdf_files:
            logging.warning("No PDF files found in the input directory.")
            return []

        results = []
        for pdf_file in pdf_files:
            pdf_path = os.path.join(self.input_dir, pdf_file)
            try:
                doc = fitz.open(pdf_path)
                for page_num in range(len(doc)):
                    page = doc.load_page(page_num)
                    text = page.get_text("text")
                    sentences = sent_tokenize(text)

                    # Save sentences to a text file
                    output_file_path = os.path.join(
                        self.output_dir, f"{os.path.splitext(pdf_file)[0]}_page_{page_num + 1}"
                    )
                    with open(output_file_path, "w") as f:
                        f.write("\n".join(sentences))

                    results.append(output_file_path)

                doc.close()
            except Exception as e:
                logging.error(f"Error processing file {pdf_file}: {e}")

        return results