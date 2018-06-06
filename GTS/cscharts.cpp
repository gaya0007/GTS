#include "cscharts.h"

CSCharts::CSCharts(QString name)
{
    chart = new QChart();

    series = new QCandlestickSeries();
    series->setName(name);
    series->setIncreasingColor(QColor(Qt::green));
    series->setDecreasingColor(QColor(Qt::red));
}

bool CSCharts::setup_chart()
{
    bool ret = false;
    chart->addSeries(series);
    chart->setAnimationOptions(QChart::SeriesAnimations);

    chart->createDefaultAxes();

    QBarCategoryAxis *axisX = qobject_cast<QBarCategoryAxis *>(chart->axes(Qt::Horizontal).at(0));

    QValueAxis *axisY = qobject_cast<QValueAxis *>(chart->axes(Qt::Vertical).at(0));
    axisY->setMax(axisY->max() * 1.01);
    axisY->setMin(axisY->min() * 0.99);

    chart->legend()->setVisible(true);
    chart->legend()->setAlignment(Qt::AlignBottom);

    QChartView *chartView = new QChartView(chart);
    chartView->setRenderHint(QPainter::Antialiasing);

    return ret;
}
