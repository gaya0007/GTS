#ifndef MAINGUI_H
#define MAINGUI_H

#include <QtWidgets>
#include <QDialog>
#include <QDateEdit>
#include "cscharts.h"

class MainTab;

class MainGUI : public QDialog
{
    Q_OBJECT
public:
    MainGUI(QWidget *parent = 0);
    void log(QString txt);
public slots:

private:
    QLineEdit *fileNameEdit;
    QPlainTextEdit *logoutput;
    QTabWidget *tabWidget;
    MainTab * m_main_tab;
    QChartView *chartView;
};

class MainTab : public QWidget
{
    Q_OBJECT
public slots:
    void fromDateChanged(const QDate &date);
public:
    explicit MainTab(QWidget *parent = 0);
    QComboBox *pairs;
    QDateEdit *from_date;
    QDateEdit *to_date;
    QComboBox *timeframes;
private:


};
#endif // MAINGUI_H
