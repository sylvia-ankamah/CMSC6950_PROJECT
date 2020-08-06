processed_data.pkl:daily-total-female-births.csv project.py
	python3 project.py

Birth_data_Trend_plot.png: processed_data.pkl make_Trend_plot1.py
	python3 Trend_plot1.py

BIRTH_DATA_ACF_PLOT.png: processed_data.pkl  make_ACF_plot1.py
	python3 ACF_plot1.py

Birth_data_Trendline.png: processed_data.pkl make_Trendline_plot1.py
	python3 Trendline_plot1.py

.PHONY: clean almost_clean
	rm Birth_data_Trend_plot.png
	rm BIRTH_DATA_ACF_PLOT.png
	rm Birth_data_Trendline.png

almost_clean:
	latexmk -c
