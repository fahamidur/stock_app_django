# Screenshot
- **Line Graph** 
![Line Graph](.\image\1.JPG)

- **Candle Stick Graph** 
![Candle Stick Graph](.\image\2.JPG)

- **Data Table** 
![Data Table](.\image\3.JPG)

```markdown
# Stock Market Django App

This Django web application displays stock market data in a table and provides interactive visualizations using Plotly. The project has two branches: `master` and `feature/charts`.

## Master Branch

The `master` branch represents the baseline version of the Stock Market Django App. The main features and functionalities include:

- **Database Setup:**
  - Utilizes a PostgreSQL database to store stock market data.
  - Django models, such as `StockData`, define the structure of the data.

- **Data Loading:**
  - Includes a custom Django management command to load stock market data from a JSON fixture (`data.json`) into the PostgreSQL database.

- **Table View:**
  - Displays stock market data in a tabular format using Django templates.

## Feature/Charts Branch

The `feature/charts` branch extends the functionality of the Stock Market Django App by incorporating interactive visualizations using Plotly. Key additions include:

- **Line Graph Visualization:**
  - Adds a dynamic line graph above the table displaying closing prices over time.
  - Supports multi-axis charts with an option to select different trade codes.

- **Candlestick Chart Visualization:**
  - Introduces a candlestick chart for advanced price visualization.

- **Filtering Options:**
  - Implements a filter system in both charts to filter data by trade code.

- **Additional Styling:**
  - Improves the visual appeal with styling adjustments for the line and candlestick charts.

- **Dropdown Selector:**
  - Includes a dropdown menu in the charts to select different trade codes.

## Instructions to Run the Application:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/stock-market-django-app.git
   ```

2. **Switch to the Desired Branch:**
   ```bash
   git checkout branch-name
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Load Data:**
   ```bash
   python manage.py loaddata data.json
   ```

6. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application:**
   Open a web browser and go to [http://localhost:8000](http://localhost:8000) to view the Stock Market Django App.

Feel free to reach out if you encounter any issues or have questions!
```

Replace "your-username" and "branch-name" with your actual GitHub username and the name of the branches you have in your repository.
