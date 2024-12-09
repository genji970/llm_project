from peft import LoraConfig , get_peft_model
from param_arg import get_args

# ArgumentParser로 값 가져오기
args = get_args()

# LoRA 설정
lora_config = LoraConfig(
    r=args.r,  # Low-rank 업데이트 행렬 차원
    lora_alpha=args.lora_alpha,  # 스케일링 팩터
    lora_dropout=args.lora_dropout,  # 드롭아웃 비율
    target_modules=args.target_modules,  # QLoRA가 적용될 대상 모듈
)

