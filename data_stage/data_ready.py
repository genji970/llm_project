import os
import logging

class Data_Ready():

    def __init__(self , input_dir):
        self.input_dir = input_dir

    @property
    def data_ready(self : 'str') -> 'str':

        try:
            if os.path.isdir(self.input_dir):
                logger.info(f"The input_dir '{self.input_dir}' is a valid directory.")

                return self.input_dir , "directory"

            elif self.input_dir.startswith("http://") or self.input_dir.startswith("https://"):
                logger.info(f"The input_dir '{self.input_dir}' is a valid URL.")
                return self.input_dir , "url"
            else:
                # input_dir가 존재하지 않는 경우
                if not os.path.exists(self.input_dir):
                    logger.error(f"The input_dir '{self.input_dir}' does not exist.")
                    raise FileNotFoundError(f"The input_dir '{self.input_dir}' does not exist.")
                else:
                    logger.warning(f"The input_dir '{self.input_dir}' is neither a directory nor a URL.")
                    raise FileNotFoundError("unknown")
        except Exception as e:
            logger.exception(f"An error occurred: {e}")
            raise



