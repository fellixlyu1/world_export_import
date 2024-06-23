<p>This GUI application allows the user to create and save png files of either a scatter plot graph or a pie chart, depending on the csv file provided by the user. In this project,
the GUI app uses a Kaggle dataset that contains a "a comprehensive collection of data related to international trade and trade policies". If the user needs this tool for their
data analysis, the user will need to access the 'csv_to_sql' folder.</p>

<p>Within the folder, the user can transfer the csv file that they want to create into a table and a database. If the user needs to join other tables into the database, they will 
have to create separate statements.</p>

<h1><strong>RUN THE PROGRAM</strong></h1>
<p>Once the user runs the program, a GUI window will pop up and show two choices: 'Scatter Plot' or 'Pie Chart'. Depending on which button the user picks, the application will open
the selected window.</p>

![Screenshot 2024-06-23 9 19 51 AM](https://github.com/fellixlyu1/world_export_import/assets/116593040/e9725df1-ccdb-4e3e-916c-d9fb3f8a0356)

<h3><strong>SCATTER PLOT</strong></h3>
<p>Once the Scatter Plot window appears, the user will have the option of choosing one of the 208 countries in the following csv file and the option of choosing which data type the
user requires.</p>

![Screenshot 2024-06-23 9 21 50 AM](https://github.com/fellixlyu1/world_export_import/assets/116593040/caa13bcd-f998-40e8-8467-2b60fddf3b62)

<h5><strong>Scatter Plot Example</strong></h5>

<p>The Scatter Plot window will appear and the user can click on each of the options and a scrollbar for the respective options will offer a selection of the countries and the
columns in the table, displaying options for: 'Countries' and 'Data'.</p>

<p>In this example, the user will use 'Bulgaria' for the country and 'AHS AVE Tariff Share Lines' in the GUI window.</p>

![Screenshot 2024-06-23 9 22 34 AM](https://github.com/fellixlyu1/world_export_import/assets/116593040/d16d8ca7-6cff-42d3-ad52-73c59fe53457)

![Screenshot 2024-06-23 9 22 46 AM](https://github.com/fellixlyu1/world_export_import/assets/116593040/f50a7ce2-9f27-42fc-a487-a49b6dbb5a3b)

<p>Using these options, the user can close both windows and the png file will be saved in the project's folder.</p>

![Bulgaria_AHS AVE Tariff Lines Share_scatter](https://github.com/fellixlyu1/world_export_import/assets/116593040/4a571a48-c31c-4b16-ab3b-4b6f29a52bc6)

<h3><strong>PIE CHART</strong></h3>
<p>The user will have a separate window for retrieving both the data and the visualizations of the table in the 'global_imp_exp.db' database. The options, however, are different
for the user: 'Years' and 'Data'.</p>

<h5><strong>PIE CHART EXAMPLE</strong></h5>

<p></p>

<h2><strong>USING OTHER DATASETS AND CSV FILES</strong></h2>

<p>The user opens the 'python_csv.py' file and at the bottom of their IDE, the user types in the name of their csv file in the 'csv_path' variable.</p>

![csv_path](https://github.com/fellixlyu1/world_export_import/assets/116593040/05f31a8b-aaa4-422c-bf59-13249d51fe00)

<p>Now that the user has the csv path, they'll need to offer the arguments related to the parameters of the 'dataframe_to_sql' method. The second parameter will act as the name of
the database, and the third parameter will act as the table name.</p>

![names](https://github.com/fellixlyu1/world_export_import/assets/116593040/8833f6b6-1a86-4783-80c1-64cffde22ef1)

