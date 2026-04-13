import gradio as gr
from openenv_env import SupportRoutingEnv, BaselineAgent

env = SupportRoutingEnv()
agent = BaselineAgent()

def run_task(difficulty):
    state = env.reset(difficulty)
    text = str(state.get("text", ""))

    action = agent.predict(text)

    department = str(action.get("department", "unknown"))
    priority = str(action.get("priority", "low"))

    result = env.step(action)
    reward = float(result.get("reward", 0))

    return text, department, priority, reward  

with gr.Blocks() as app:
    gr.Markdown("# 🤖 Smart Support Routing AI")

    difficulty = gr.Dropdown(["easy", "medium", "hard"], value="easy")

    btn = gr.Button("Run")

    out1 = gr.Textbox(label="Ticket")
    out2 = gr.Textbox(label="Department")
    out3 = gr.Textbox(label="Priority")
    out4 = gr.Number(label="Reward")

    btn.click(run_task, inputs=difficulty, outputs=[out1, out2, out3, out4])

app.launch(server_name="0.0.0.0", server_port=7860, share=True)