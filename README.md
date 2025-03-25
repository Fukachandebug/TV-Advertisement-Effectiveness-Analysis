## 📺 TV Advertising Placement Optimization
This is a project from my participation in 2020 & 2021 [Marketing Analysis Competition](https://www.is.nri.co.jp/contest/2021/report.html) hosted by Nomura Research Institute.  
The competition aimed to propose advertising marketing strategies based on insights gained through data analysis from diverse perspevtives.  
I was awarded as a **Top Finalist** out of 110+ teams for **2 consecutive years**.

### 🎯 Objective
In this project, I developed an optimized TV advertising placement strategy.
1) Identify the optimal ad viewing frequency that maximizes purchase intention.
2) Determine the relationship between the optimal viewing frequency and ad content features.
3) Develop the standards of ad placement based on the results of 1) and 2).

Definition of optimal ad viewing frequency:  
This is equal to the maximum of the ad effectiveness.  
The lower the optimal ad viewing frequency is, the more quickly the effectiveness of ad appears.

### 📁 Dataset Used
Data is provided by Nomura Research Institute, so it cannot be opened in public.
- Survey data
  - Responses from 3,000 individuals aged 20–59 residing, including ad viewing frequency and purchase intent.
- TV programs viewing Data
  - Individual viewing history of TV programs.
- TV ad placement data
  - Information on the broadcasting schedule of TV commercials by program.

### ⚙️ Data Processing & Aggregation
Agreagated the percentage of purchase intention from survey responses and ad viewing frequency each products.  
Below is one of the results.  
When the viewing frequency is 6-10 times, purchase intent is the highest. But after 10 times viewing, purchase intent is not increased.  
-> Hypothesis: It is estimated that the effectiveness of ad may differ by viewing frequency.

### 📊 Analysis
#### Step1: Analysis of optimal ad viewing frequency
Used **generalized propensity score analysis** to estimate the optimal ad viewing frequency for 50 products.

#### Step2: Analysis of optimal ad viewing frequency and content features
Applied **multiple correspondence analysis** to determine the relationship between ad features (e.g., featured actors, narration, BGM) and optimal viewing frequency.

#### Step3: Optimization of advertising placement
Utilized **linear programming** to determine the number of placements per time slot based on different target audiences while meeting optimal viewing frequency.

### 💡 Analysis Results & Insights
#### Step1: Optimal ad viewing frequency varies by products
The result of analysis shows the optimal viewing frequency differs depending on products as implied in the result of data aggregation.

#### Step2: Optimal ad viewing frequency varies by ad features
Interestingly, it is turned out that the ad features include featured actors/actoress, creative BGM with lyrics of company's and product's name when the optimal viewing frequency is the lowest like 1-3 times. This implies that the ad whose effectiveness appears the most quickly tends to have the impactful and visual features.  
On the contrary, it is found that ad features don't tend to have creative BGM when the optimal viewing frequency is the highest like more than 10 times. This implies that the effectiveness of ad appears the latest because the lack of impactful audio makes people less attention to ad and hard to imagine produtct itself. 

#### Step3: Cost effectiveness ad placement for each target audience


