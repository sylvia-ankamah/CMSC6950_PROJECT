
plots=Birth_data_Trend_plot.png BIRTH_DATA_ACF_PLOT.png Birth_data_Trendline.png Shampoo_data_Trend_plot.png \
      SHAMPOO_DATA_ACF_PLOT.png SHAMPOO_DATA_TRENDLINE.png Malaria_Trend_plot.png MALARIA_DATA_ACF_PLOT.png 
       

Report.pdf: Report.tex $(plots) project.py  
	latexmk -pdf
	
Birth_data_Trend_plot.png: Trend_plot1.py daily-total-female-births.csv
	        python3 Trend_plot1.py

BIRTH_DATA_ACF_PLOT.png: ACF_plot1.py daily-total-female-births.csv
	        python3 ACF_plot1.py

Birth_data_Trendline.png: Trendline_plot1.py daily-total-female-births.csv
	        python3 Trendline_plot1.py

Shampoo_data_Trend_plot.png: Trend_plot2.py shampoo.csv
	        python3 Trend_plot2.py

SHAMPOO_DATA_ACF_PLOT.png: ACF_plot2.py shampoo.csv
	        python3 ACF_plot2.py

SHAMPOO_DATA_TRENDLINE.png: Trendline_plot2.py shampoo.csv
	        python3 Trendline_plot2.py


Malaria_Trend_plot.png: Trend_plot3.py Malaria_data.csv
	        python3 Trend_plot3.py

MALARIA_DATA_ACF_PLOT.png: ACF_plot3.py Malaria_data.csv
	        python3 ACF_plot3.py

.PHONY: clean almost_clean
	
clean:
	
	
	rm -f $(plots)
	rm -f Report.pdf
almost_clean:
	latexmk -c
