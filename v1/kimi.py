from openai import OpenAI

client = OpenAI(
    api_key="Your api",
    base_url="https://api.moonshot.cn/v1",
)

def get_user_input(prompt):
    return input(prompt).strip()

def generate_tour_plans(destination, history, n=3):
    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=history,
        temperature=0.3,
        n=n
    )
    return [choice.message.content for choice in completion.choices]

def save_plans_to_files(plans, destination):
    for i, plan in enumerate(plans):
        file_name = f"{destination}旅游计划{i+1}.txt"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(plan)
        print(f"旅游计划已导出到 {file_name} 文件中。")

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    destination = get_user_input("请输入旅游的目的地：")
    days = get_user_input("请输入你的旅游天数：")
    request =get_user_input("请输入你的需求：")
    # 读取景点信息和游记内容
    attraction_info = read_file(f'./景点信息/{destination}.txt')
    travel_notes = read_file(f'./游记/{destination}游记.txt')
    
    # 初始化对话历史记录
    history = [
        {
            "role": "system",
            "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"
        },
        {
            "role": "user",
            "content": f"你好，我想去{destination}旅游{days}天。"
        },
        {
            "role": "user",
            "content": f"以下是景点信息：\n{attraction_info}"
        },
        # {
        #     "role": "user",
        #     "content": f"我会给你三篇游记让你作为参考：\n{travel_notes}"
        # },
        {
            "role": "user",
            "content": f"以下是我的个性化旅游需求：{request},请你根据这些需求生成一个旅游计划"
        }
    ]
    
    # 生成初始旅游计划
    tour_plans = generate_tour_plans(destination, history)
    
    # 保存初始旅游计划
    save_plans_to_files(tour_plans, destination)
    
    while True:
        user_satisfaction = get_user_input("你对生成的旅游计划满意吗？如果不满意，请输入你的新需求（输入 '满意' 或者 '退出' 结束对话）：")
        
        if user_satisfaction in ['满意', '退出']:
            break
        
        # 添加用户的新需求到对话历史记录
        history.append({"role": "user", "content": f"{user_satisfaction},请你根据这些新的需求重新生成一个旅游计划。"})
        
        # 生成新的旅游计划
        new_tour_plans = generate_tour_plans(destination, history)
        
        # 保存新的旅游计划
        save_plans_to_files(new_tour_plans, destination)
        
        # 更新对话历史记录
        for plan in new_tour_plans:
            history.append({"role": "assistant", "content": plan})

if __name__ == "__main__":
    main()
