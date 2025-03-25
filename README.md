## 📺 TV Advertising Placement Optimization
This is a project from my participation in 2020 & 2021 [Marketing Analysis Competition](https://www.is.nri.co.jp/contest/2021/report.html) hosted by Nomura Research Institute.  
The competition aimed to propose advertising marketing strategies based on insights gained through data analysis from diverse perspevtives.  
I was awarded as a **Top Finalist** out of 110+ teams for **2 consecutive years**.

### 🎯 Objective
In this project, I developed an optimized TV advertising placement strategy.
1) Identify the optimal ad viewing frequency that maximizes purchase intention.
2) Determine the relationship between the optimal viewing frequency and ad content features.
3) Develop the standards of ad placement based on the results of 1) and 2).

Definition of Optimal ad viewing frequency:  
The lower the viewing frequency is, the effectiveness of ad appears quickly. In this case, ad cost can be mitigrated.

### 📁 Dataset Used
Data is provided by Nomura Research Institute, so it cannot be opened in public.
- Survey data
  - Responses from 3,000 individuals aged 20–59 residing, including ad viewing frequency and purchase intent.
- TV programs viewing Data
  - Individual viewing history of TV programs.
- TV ad placement data
  - Information on the broadcasting schedule of TV commercials by program.

### ⚙️ Data Processing & Aggregation
I aggreagated the percentage of purchase intention from survey responses and ad viewing frequency each products.  
Below is the result of agreegation for a payment service which is called 'PayPay'.
-> Hypothesis: It is predicted that there might be optimal viewing frequency and it varies by products.

### 📊 Analysis
#### Step1: Analysis of optimal ad viewing frequency
Used **generalized propensity score analysis** to estimate the optimal ad viewing frequency for 50 products.

#### Step2: Analysis of optimal ad viewing frequency and content features
Applied **multiple correspondence analysis** to determine the relationship between ad features (e.g., featured actors, narration, BGM) and optimal viewing frequency.

#### Step3: Optimization of advertising placement
Utilized **linear programming** to determine the number of placements per time slot based on different target audiences.

### 💡 Analysis Results & Insights
#### Step1: Optimal ad viewing frequency varies by products
The result of analysis shows the optimal viewing frequency differs depending on products as implied in the result of data aggregation.

#### Step2: Optimal ad viewing frequency is related to ad features.
Interestingly, the ad features for 1-3 times of optimal viewing frequency 




