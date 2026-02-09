from prefect import flow, task # type: ignore
import subprocess

# ===============================
# Task: Run MLflow Training Script
# ===============================
@task
def train_model():
    print("🚀 Starting MLflow Training...")
    subprocess.run(["python", "train_mlflow.py"])
    print("✅ Training Completed!")

# ===============================
# Flow Definition
# ===============================
@flow(name="Flipkart Sentiment Workflow")
def sentiment_pipeline():
    train_model()

if __name__ == "__main__":
    sentiment_pipeline.serve(
        name="flipkart-auto-training",
        interval=3600  # every 1 hour
    )
