## 📺 TV Advertising Placement Optimization
This is a project from my participation in 2020 & 2021 [Marketing Analysis Competition](https://www.is.nri.co.jp/contest/2021/report.html) hosted by Nomura Research Institute(NRI).  
The competition aimed to propose advertising marketing strategies based on insights gained through data analysis from diverse perspevtives.  
I was awarded as a **Top Finalist**🎖️ out of 110+ teams for **2 consecutive years** .

### 🎯 **Objective**
In this project, I developed an optimized TV advertising placement strategy for three key goals.
1) Identify the optimal ad viewing frequency that maximizes purchase intent.
2) Determine the relationship between optimal viewing frequency and ad content features.
3) Develop placement standards based on the insights from 1) and 2).

Definition of optimal ad viewing frequency:  
The number of times an ad needs to be viewed to maximize its effectiveness.  
The lower the optimal viewing frequency, the faster the ad achieves its maximum impact.

### 📁 **Dataset Used**
The dataset was provided by NRI and cannot be disclosed in public.  
It includes:
- Survey Data
  - Responses from 3,000 individuals aged 20–59, including ad viewing frequency and purchase intent.
- TV Programs Viewing Data
  - Individual viewing history of TV programs.
- TV Ad Placement Data
  - Broadcasting schedules of TV commercials by program.

### ⚙️ **Data Processing & Aggregation**
I agreagated the percentage of purchase intent based on survey responses and ad viewing frequency for each products.  
**Key Observation:**
- When an ad is viewed 6–10 times, purchase intent is at its highest.
- However, beyond 10 viewings, purchase intent no longer increases.
**Hypothesis:**
The effectiveness of an ad may vary depending on the number of viewings.

### 📊 **Analysis**
#### **Step1: Analysis of optimal ad viewing frequency**
Used **generalized propensity score analysis** to estimate the optimal ad viewing frequency for 50 products.

#### **Step2: Analysis of optimal ad viewing frequency and content features**
Applied **multiple correspondence analysis** to determine how ad features (e.g. featured actors, narration, BGM) influence optimal viewing frequency.

#### **Step3: Optimization of advertising placement**
Utilized **linear programming** to determine the ideal number of placements per time slot while ensuring cost efficiency and target audience reach.

### 💡 **Analysis Results & Insights**
#### **Step1: Optimal ad viewing frequency varies by products**
The analysis confirmed that the optimal viewing frequency differs depending on products as implied in the result of data aggregation.

#### **Step2: Ad features influence optimal viewing frequency**
- Ads with lower optimal viewing frequency (1–3 times) tend to have:
  ✅ Popular actors/actresses
  ✅ Creative BGM with lyrics that include the company or product name
   → These ads create a strong visual and auditory impact, making them effective more quickly.
- Ads requiring higher optimal viewing frequency (10+ times) often lack:
  ❌ Creative BGM
   → Without strong auditory impact, these ads attract less attention, making it harder for consumers to recall the product.

#### **Step3: Cost effectiveness ad placement for each target audience**


