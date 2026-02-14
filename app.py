import numpy as np
import gradio as gr


def generate_stock_data(n_days):
    n_days = int(n_days)

    days = np.array([f"Day {i + 1}" for i in range(n_days)])
    prices = np.random.randint(100, 501, (n_days, 3))

    table = np.column_stack((days, prices))

    return table, table


def daily_returns(data):
    data = np.array(data)

    days = data[:, 0]
    prices = data[:, 1:].astype(float)

    diff = np.diff(prices, axis=0)
    prev = prices[:-1]

    returns = (diff / prev) * 100

    return_days = days[1:]

    return np.column_stack((return_days, returns))


def stock_volatility(data):
    data = np.array(data)

    prices = data[:, 1:].astype(float)

    diff = np.diff(prices, axis=0)
    prev = prices[:-1]

    returns = (diff / prev) * 100

    vol = np.std(returns, axis=0)

    stocks = np.array(["Stock A", "Stock B", "Stock C"])

    return np.column_stack((stocks, vol))


def best_stock_per_day(data):
    data = np.array(data)

    days = data[:, 0]
    prices = data[:, 1:].astype(float)

    diff = np.diff(prices, axis=0)
    prev = prices[:-1]

    returns = (diff / prev) * 100

    return_days = days[1:]

    idx = np.argmax(returns, axis=1)

    stocks = np.array(["Stock A", "Stock B", "Stock C"])

    best_stocks = stocks[idx]
    best_returns = returns[np.arange(len(returns)), idx]

    return np.column_stack((return_days, best_stocks, best_returns))


with gr.Blocks(title="Stock Market Analyzer") as demo:

    gr.Markdown("# 📈 Stock Market Mini Analyzer")

    data_state = gr.State()

    with gr.Row():
        days_input = gr.Number(value=10, label="Number of Days")
        generate_btn = gr.Button("Generate Stock Data", variant="primary")

    stock_table = gr.Dataframe(
        headers=["Day", "Stock A", "Stock B", "Stock C"],
        interactive=False
    )

    generate_btn.click(
        generate_stock_data,
        inputs=days_input,
        outputs=[data_state, stock_table]
    )

    gr.Markdown("---")

    with gr.Tab("📊 Daily Returns"):
        return_btn = gr.Button("Compute Daily Returns", variant="primary")
        return_output = gr.Dataframe(
            headers=["Day", "Return A (%)", "Return B (%)", "Return C (%)"],
            interactive=False
        )
        return_btn.click(daily_returns, inputs=data_state, outputs=return_output)

    with gr.Tab("📉 Volatility"):
        vol_btn = gr.Button("Compute Volatility", variant="primary")
        vol_output = gr.Dataframe(
            headers=["Stock", "Volatility (%)"],
            interactive=False
        )
        vol_btn.click(stock_volatility, inputs=data_state, outputs=vol_output)

    with gr.Tab("🏆 Best Stock Per Day"):
        best_btn = gr.Button("Find Best Performer", variant="primary")
        best_output = gr.Dataframe(
            headers=["Day", "Best Stock", "Return (%)"],
            interactive=False
        )
        best_btn.click(best_stock_per_day, inputs=data_state, outputs=best_output)

demo.launch(theme=gr.themes.Soft())
