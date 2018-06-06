#ifndef CSCHARTS_H
#define CSCHARTS_H

#include <QtCharts/QBarCategoryAxis>
#include <QtCharts/QCandlestickSeries>
#include <QtCharts/QChartView>
#include <QtCharts/QValueAxis>
#include <QtCore/QDateTime>

QT_CHARTS_USE_NAMESPACE

class CSCharts
{
public:
    CSCharts(QString name);
    bool addCandle();
    bool setup_chart();
private:
    QChart *chart;
    QCandlestickSeries *series;
};

#endif // CSCHARTS_H
