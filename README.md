<<<<<<< HEAD
# sales_prediction_ml_model



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

* [Create](https://docs.gitlab.com/user/project/repository/web_editor/#create-a-file) or [upload](https://docs.gitlab.com/user/project/repository/web_editor/#upload-a-file) files
* [Add files using the command line](https://docs.gitlab.com/topics/git/add_files/#add-files-to-a-git-repository) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.com/suniljaswani.it/sales_prediction_ml_model.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

* [Set up project integrations](https://gitlab.com/suniljaswani.it/sales_prediction_ml_model/-/settings/integrations)

## Collaborate with your team

* [Invite team members and collaborators](https://docs.gitlab.com/user/project/members/)
* [Create a new merge request](https://docs.gitlab.com/user/project/merge_requests/creating_merge_requests/)
* [Automatically close issues from merge requests](https://docs.gitlab.com/user/project/issues/managing_issues/#closing-issues-automatically)
* [Enable merge request approvals](https://docs.gitlab.com/user/project/merge_requests/approvals/)
* [Set auto-merge](https://docs.gitlab.com/user/project/merge_requests/auto_merge/)

## Test and Deploy

Use the built-in continuous integration in GitLab.

* [Get started with GitLab CI/CD](https://docs.gitlab.com/ci/quick_start/)
* [Analyze your code for known vulnerabilities with Static Application Security Testing (SAST)](https://docs.gitlab.com/user/application_security/sast/)
* [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/topics/autodevops/requirements/)
* [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/user/clusters/agent/)
* [Set up protected environments](https://docs.gitlab.com/ci/environments/protected_environments/)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thanks to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README

Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
=======
# 🏪 Sales Prediction by Store (ML + FastAPI + Flask)

This project builds a Machine Learning model to predict store sales based on features like store details, promotions, holidays, and customer count.

It supports:

* ✅ Batch prediction from SQLite DB
* ✅ Real-time prediction via API
* ✅ FastAPI with Swagger UI
* ✅ Flask API

---

# 🚀 1. Project Setup

## 🔹 Clone the Repository

```bash
git clone <your-repo-url>
cd Sales_Prediction_By_Store
```

---

## 🔹 Install Dependencies (Using uv)

Make sure Python 3.12+ is installed.

```bash
pip install uv
uv sync
```

---

# 📂 2. Project Structure

```
Sales_Prediction_By_Store/
│
├── db_operations/              # SQLite data loading
├── common_operations/          # Preprocessing logic
├── model_training/             # Training script
├── batch_prediction_script/    # Batch prediction
│
├── app.py                      # Flask API
├── fastapi_app.py              # FastAPI (Swagger)
│
├── model.pkl                   # Trained model
├── columns.pkl                 # Feature columns
├── regression.db               # SQLite database
├── pyproject.toml
```

---

# 🧠 3. Train the Model

Train using first 700k records:

```bash
uv run python -m model_training.train_model
```

This will:

* Train XGBoost model
* Save `model.pkl`
* Save `columns.pkl`

---

# 📊 4. Batch Prediction

Run prediction on next 200k records:

```bash
uv run python -m batch_prediction_script.predict
```

---

# ⚡ 5. Run FastAPI (Recommended)

Start API:

```bash
uv run uvicorn fastapi_app:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# 🔮 6. Real-Time Prediction API

### Endpoint:

```
POST /predict
```

### Sample Request:

```json
{
  "Store": 1,
  "DayOfWeek": 3,
  "Date": "2024-01-15",
  "Customers": 200,
  "Open": 1,
  "Promo": 1,
  "StateHoliday": "0",
  "SchoolHoliday": 0
}
```

### Sample Response:

```json
{
  "predicted_sales": 5352.22
}
```

---

# 🗄️ 7. Batch Prediction from SQLite DB

### Endpoint:

```
POST /predict-from-db
```

### Sample Request:

```json
{
  "db_path": "D:/path/to/regression.db",
  "limit": 10,
  "offset": 0
}
```

### Sample Response:

```json
{
  "total_records": 10,
  "predictions_sample": [
    {
      "Store": 1,
      "Date": "2015-07-31",
      "Customers": 555,
      "Promo": 1,
      "PredictedSales": 5352.22
    }
  ]
}
```

---

# 🌐 8. Run Flask API (Alternative)

```bash
uv run python app.py
```

Endpoint:

```
POST http://127.0.0.1:5000/predict
```

---

# ⚠️ 9. Important Notes

* Ensure `regression.db` path is correct
* Always use valid date format:

  ```
  YYYY-MM-DD
  ```
* Model uses:

  * Feature engineering (Date → Year, Month, Day)
  * One-hot encoding
* Column consistency handled via `columns.pkl`

---

# 📈 10. Model Details

* Model: XGBoost Regressor
* Evaluation Metrics:

  * MAE (Mean Absolute Error)
  * R² Score
* Features:

  * Store, Customers, Promo, Holidays, Date features

---

# 🏁 11. End-to-End Flow

```
SQLite DB → Preprocessing → Model Training → Save Model
                                   ↓
                           API Prediction
```

---

# 🤖 12. Machine Learning Model Details

---

## 🔹 ML Model Selected

The project uses **XGBoost Regressor** for predicting store sales.

### Why XGBoost?

* Works very well for **structured/tabular data**
* Handles **non-linear relationships**
* Provides **high accuracy** compared to traditional models
* Built-in support for **feature importance**
* Efficient for **large datasets (1M records)**

---

## 🔹 Features Selected

### Original Features Used:

* **Store** → Store ID
* **DayOfWeek** → Day of the week
* **Customers** → Number of customers visiting the store
* **Open** → Whether store is open or closed
* **Promo** → Promotion running (1/0)
* **StateHoliday** → State holiday indicator
* **SchoolHoliday** → School holiday indicator

---

### Feature Engineering:

The `Date` column was transformed into:

* **Year**
* **Month**
* **Day**

👉 This helps the model learn:

* Seasonal trends
* Monthly sales patterns
* Daily variations

---

### Encoding:

* Categorical features like `StateHoliday` are converted using:

  ```python
  pd.get_dummies()
  ```

---

## 🔹 Feature Importance

Feature importance is extracted using:

```python
model.feature_importances_
```

### Key Observations:

* **Customers** → Most influential feature (higher customers = higher sales)
* **Promo** → Promotions significantly increase sales
* **Open** → Sales occur only when store is open
* **Month / Day** → Capture seasonal trends
* **DayOfWeek** → Weekly behavior patterns

---

## 🔹 Evaluation of the Model

The model is evaluated using:

### 1. Mean Absolute Error (MAE)

* Measures average prediction error
* Lower value = better performance

Example:

```
MAE: 800
```

👉 On average, predictions are off by ~800 sales units.

---

### 2. R² Score (R-Squared)

* Measures how well the model explains variance
* Range: 0 to 1

Example:

```
R2: 0.92
```

👉 Model explains **92% of the variation in sales data**.

---

## 🔹 Data Splitting Strategy

* **700,000 records** → Training
* **200,000 records** → Validation
* **100,000 records** → Simulated production

---

## 🔹 Deployment

The model is deployed using:

* **Batch prediction script** (for bulk processing)
* **Flask API** (real-time prediction)
* **FastAPI (Swagger UI)** (interactive API testing)

---

## 🔹 Summary

* XGBoost model provides high accuracy for sales prediction
* Feature engineering improves model performance
* Evaluation metrics confirm strong predictive capability
* APIs enable both batch and real-time predictions

# 👨‍💻 Author

Sunil Jaswani
>>>>>>> 5dfe803 (Initial commit)
