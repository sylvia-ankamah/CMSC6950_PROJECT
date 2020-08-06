data1:daily-total-female-births.csv project.py
	python3 project.py

Birth_data_Trend_plot.png: data1 make_Trend_plot1.py
	python3 Trend_plot1.py

BIRTH_DATA_ACF_PLOT.png: data1  make_ACF_plot1.py
	python3 ACF_plot1.py

Birth_data_Trendline.png: datal make_Trendline_plot1.py
	python3 Trendline_plot1.py

data2:shampoo.csv project.py
	python3 project.py

Shampoo_data_Trend_plot.png: data2 make_Trend_plot2.py
	python3 Trend_plot2.py

SHAMPOO_DATA_ACF_PLOT.png: data2 make_ACF_plot2.py
	python3 ACF_plot2.py

SHAMPOO_DATA_TRENDLINE.png: data2 make_Trendline_plot2.py
	python3 Trendline_plot2.py

data3:Malaria_data.csv project.py
	python3 project.py

Malaria_Trend_plot.png: data3 make_Trend_plot3.py
	python 3 Trend_plot3.py

MALARIA_DATA_ACF_PLOT.png: data3 make_ACF_plot3.py
	python 3 ACF_plot3.py

.PHONY: clean almost_clean
	rm Birth_data_Trend_plot.png
	rm BIRTH_DATA_ACF_PLOT.png
	rm Birth_data_Trendline.png
	rm Shampoo_data_Trend_plot.png
	rm SHAMPOO_DATA_ACF_PLOT.png
	rm SHAMPOO_DATA_TRENDLINE.png
	rm Malaria_Trend_plot.png
	rm MALARIA_DATA_ACF_PLOT.png



almost_clean:
	latexmk -c
