#ifndef MAINGUI_H
#define MAINGUI_H

#include <QtWidgets>
#include <QDialog>
#include <QDateEdit>
#include "cscharts.h"
#include "ipc.h"

class MainTab;

class MainGUI : public QDialog
{
    Q_OBJECT
public:
    MainGUI(QWidget *parent = 0);
    void log(QString txt);
public slots:

private:
    IPC *ipc;
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
    void btn_click_analyze();
public:
    explicit MainTab(QWidget *parent = 0);
    QComboBox *pairs;
    QDateEdit *from_date;
    QDateEdit *to_date;
    QComboBox *timeframes;
    QPushButton *btn_analyze;
private:


};
#endif // MAINGUI_H
