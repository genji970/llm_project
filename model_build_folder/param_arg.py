import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Configuration")
    parser.add_argument("--r", type=int, default=8, help="Low-rank update matrix dimension (r)")
    parser.add_argument("--lora_alpha", type=int, default=16, help="Scaling factor (LoRA Alpha)")
    parser.add_argument("--lora_dropout", type=float, default=0.1, help="Dropout rate for LoRA")
    parser.add_argument("--target_modules", nargs='+', default=["q_proj", "k_proj", "v_proj", "out_proj"], help="Target modules for LoRA")

    parser.add_argument("--model_name", type=str, default= 'gpt2', help="model_name")
    parser.add_argument("--device_map" , type=str , default = 'auto' , help = 'device_map')
    parser.add_argument("torch_dtype", type=str,default = 'auto', help = 'torch_dtype')
    parser.add_argument("offload_folder",type=str,default = "./offload",help='offload_folder')
    parser.add_argument("offload_state_dict",type=bool,default = True , help = 'offload_state_dict')

    return parser.parse_args()



