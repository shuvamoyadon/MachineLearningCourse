<h2 style="color:#4F8EF7;">Quantiles: Breaking Data into Equal Parts</h2>

Quantiles are values that divide your data into equal-sized chunks. For example, if you have 100 students' scores, quantiles help you see who is in the top 25%, middle 50%, etc.

<b>Types of Quantiles:</b>
- <b>Quartiles</b>: Divide data into 4 parts (Q1, Q2, Q3)
- <b>Quintiles</b>: Divide data into 5 parts
- <b>Deciles</b>: Divide data into 10 parts
- <b>Percentiles</b>: Divide data into 100 parts

<h3 style="color:#F78E4F;">Example: Student Test Scores</h3>
Suppose we have these scores: <b>55, 60, 65, 70, 75, 80, 85, 90, 95, 100</b>

- <b>Q1 (25th percentile):</b> 65 (25% of students scored below 65)
- <b>Q2 (Median/50th percentile):</b> 77.5 (half scored below, half above)
- <b>Q3 (75th percentile):</b> 90 (75% scored below 90)

<h2 style="color:#4FCF8E;">Percentiles: Ranking Data</h2>

Percentiles show the percentage of data below a certain value.

<b>Example:</b> If your score is in the 80th percentile, you did better than 80% of people.

<h3 style="color:#F74F8E;">Percentile Example with Heights</h3>
Suppose the heights (in cm) of 10 kids: <b>120, 122, 125, 127, 130, 132, 135, 137, 140, 145</b>
- The 90th percentile is 143.5 cm (only 10% are taller)
- The 50th percentile (median) is 131 cm

<h2 style="color:#F7D24F;">Visual Representation</h2>

<pre style="background:#f0f8ff; color:#333;">
|---Q1---|---Q2---|---Q3---|---Q4---|
|  65   | 77.5  |  90   | 100  |
</pre>

<h2 style="color:#4F8EF7;">Summary</h2>
Quantiles and percentiles help us understand how data is spread out and where a particular value stands in a group. They're super useful for comparing scores, heights, or any measurements!

<h2 style="color:#8E44AD;">Five Number Summary</h2>

The <b>Five Number Summary</b> gives you a quick snapshot of your data's spread. It includes:
<ul>
  <li><b>Minimum</b>: The smallest value</li>
  <li><b>Q1 (First Quartile)</b>: 25% of data falls below this value</li>
  <li><b>Median (Q2)</b>: The middle value</li>
  <li><b>Q3 (Third Quartile)</b>: 75% of data falls below this value</li>
  <li><b>Maximum</b>: The largest value</li>
</ul>

<h3 style="color:#16A085;">Example: Student Test Scores</h3>
Suppose we have these scores: <b>55, 60, 65, 70, 75, 80, 85, 90, 95, 100</b>
<ul>
  <li><b>Minimum:</b> 55</li>
  <li><b>Q1:</b> 65</li>
  <li><b>Median:</b> 77.5</li>
  <li><b>Q3:</b> 90</li>
  <li><b>Maximum:</b> 100</li>
</ul>

This summary helps you quickly see the range and where most values are clustered!


<h2 style="color:#E67E22;">Box Plot</h2>

A <b>Box Plot</b> (or box-and-whisker plot) is a simple graph that shows the spread of data using the five number summary: minimum, Q1, median, Q3, and maximum.

<ul>
  <li>The <b>box</b> shows the middle 50% of the data (from Q1 to Q3).</li>
  <li>The <b>line</b> inside the box is the median.</li>
  <li>The <b>whiskers</b> stretch to the minimum and maximum values.</li>
</ul>

<h3 style="color:#2980B9;">Example: Student Test Scores</h3>
Suppose we have these scores: <b>55, 60, 65, 70, 75, 80, 85, 90, 95, 100</b>

Below is a simple box plot for these scores:

<svg width="400" height="100" xmlns="http://www.w3.org/2000/svg">
  <!-- Whiskers -->
  <line x1="40" y1="50" x2="360" y2="50" stroke="#888" stroke-width="2"/>
  <!-- Min -->
  <rect x="35" y="40" width="10" height="20" fill="#16A085"/>
  <text x="30" y="80" font-size="12">55</text>
  <!-- Q1 -->
  <rect x="100" y="35" width="10" height="30" fill="#2980B9"/>
  <text x="95" y="80" font-size="12">65</text>
  <!-- Box -->
  <rect x="100" y="40" width="160" height="20" fill="#F9E79F" stroke="#2980B9" stroke-width="2"/>
  <!-- Median -->
  <line x1="180" y1="35" x2="180" y2="75" stroke="#E74C3C" stroke-width="3"/>
  <text x="170" y="80" font-size="12">77.5</text>
  <!-- Q3 -->
  <rect x="250" y="35" width="10" height="30" fill="#2980B9"/>
  <text x="245" y="80" font-size="12">90</text>
  <!-- Max -->
  <rect x="355" y="40" width="10" height="20" fill="#16A085"/>
  <text x="350" y="80" font-size="12">100</text>
</svg>

This plot helps you quickly see where most scores are, the median, and any potential outliers!

<h2 style="color:#27AE60;">Scatter Plot</h2>

A <b>Scatter Plot</b> is a graph that shows the relationship between two variables. Each point represents a pair of values.

<ul>
  <li>Helps you see patterns, trends, or correlations.</li>
  <li>If the points go up together, it's a positive relationship. If one goes up while the other goes down, it's negative.</li>
</ul>

<h3 style="color:#8E44AD;">Example: Study Hours vs. Test Scores</h3>
Suppose we have data for 8 students:
<ul>
  <li>Hours Studied: 1, 2, 3, 4, 5, 6, 7, 8</li>
  <li>Test Scores: 55, 60, 62, 68, 72, 75, 80, 85</li>
</ul>

Below is a simple scatter plot for these values:

<svg width="350" height="200" xmlns="http://www.w3.org/2000/svg">
  <!-- Axes -->
  <line x1="40" y1="160" x2="320" y2="160" stroke="#333" stroke-width="2"/>
  <line x1="40" y1="160" x2="40" y2="40" stroke="#333" stroke-width="2"/>
  <!-- Points -->
  <circle cx="60" cy="150" r="6" fill="#27AE60"/>
  <circle cx="80" cy="140" r="6" fill="#2980B9"/>
  <circle cx="100" cy="135" r="6" fill="#E67E22"/>
  <circle cx="120" cy="125" r="6" fill="#8E44AD"/>
  <circle cx="160" cy="110" r="6" fill="#F1C40F"/>
  <circle cx="200" cy="95" r="6" fill="#E74C3C"/>
  <circle cx="250" cy="75" r="6" fill="#16A085"/>
  <circle cx="300" cy="60" r="6" fill="#34495E"/>
  <!-- Labels -->
  <text x="20" y="165" font-size="12">0</text>
  <text x="320" y="175" font-size="12">Hours</text>
  <text x="5" y="45" font-size="12">Score</text>
</svg>

This plot helps you see that as study hours increase, test scores also go up—a positive relationship!

<h2 style="color:#C0392B;">Covariance and Correlation</h2>

<b>Covariance</b> and <b>Correlation</b> both measure how two variables move together, but correlation is easier to interpret.

<ul>
  <li><b>Covariance</b>: Tells you if two variables increase or decrease together. Positive means they move in the same direction, negative means opposite.</li>
  <li><b>Correlation</b>: Standardizes covariance to a value between -1 and 1. +1 means perfect positive relationship, -1 means perfect negative, 0 means no relationship.</li>
</ul>

<h3 style="color:#2980B9;">Example: Study Hours vs. Test Scores</h3>
Suppose we have data for 5 students:
<ul>
  <li>Hours Studied: 2, 4, 6, 8, 10</li>
  <li>Test Scores: 60, 65, 70, 80, 85</li>
</ul>

- The covariance is positive, so as study hours increase, scores increase.
- The correlation is close to +1, showing a strong positive relationship.

<svg width="350" height="200" xmlns="http://www.w3.org/2000/svg">
  <!-- Axes -->
  <line x1="40" y1="160" x2="320" y2="160" stroke="#333" stroke-width="2"/>
  <line x1="40" y1="160" x2="40" y2="40" stroke="#333" stroke-width="2"/>
  <!-- Points -->
  <circle cx="60" cy="150" r="7" fill="#C0392B"/>
  <circle cx="110" cy="130" r="7" fill="#C0392B"/>
  <circle cx="160" cy="110" r="7" fill="#C0392B"/>
  <circle cx="210" cy="80" r="7" fill="#C0392B"/>
  <circle cx="270" cy="60" r="7" fill="#C0392B"/>
  <!-- Trend Line -->
  <line x1="60" y1="150" x2="270" y2="60" stroke="#2980B9" stroke-width="3"/>
  <!-- Labels -->
  <text x="20" y="165" font-size="12">0</text>
  <text x="320" y="175" font-size="12" fill="#fff">Hours</text>
  <text x="5" y="45" font-size="12" fill="#fff">Score</text>
</svg>

This graph shows that as hours studied go up, test scores also go up—a strong positive correlation!