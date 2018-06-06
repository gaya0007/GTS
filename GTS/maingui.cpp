#include "maingui.h"

class QScreen;

MainGUI::MainGUI(QWidget *parent):QDialog(parent)
{
    QScreen *screen = QGuiApplication::primaryScreen();
    int window_height = screen->geometry().height();
    int window_width = screen->geometry().width();
    /*creating a tab widget*/
    tabWidget = new QTabWidget;

    chartView = new QChartView;
    chartView->setFixedWidth(window_width - 500);
    chartView->setFixedHeight(window_height - 200);

    m_main_tab = new MainTab(this);
    m_main_tab->setFixedWidth(400);
    tabWidget->addTab(m_main_tab, tr("Main"));

    logoutput = new QPlainTextEdit;

    QHBoxLayout *AppLayout = new QHBoxLayout;
    AppLayout->addWidget(tabWidget);
    AppLayout->addWidget(chartView);

    QVBoxLayout *mainLayout = new QVBoxLayout;
    mainLayout->addLayout(AppLayout);
    mainLayout->addWidget(logoutput);
    setLayout(mainLayout);

    setWindowTitle(tr("GTS"));
}


MainTab::MainTab(QWidget *parent) : QWidget(parent)
{
    pairs = new QComboBox;
    timeframes = new QComboBox;
    pairs->addItem(tr("EURUSD"));
    QStringList tfl = {tr("15M"),tr("30M"), tr("1H"), tr("4H"), tr("24H")};
    timeframes->addItems(tfl);
    from_date = new QDateEdit();
    from_date->setCalendarPopup(true);
    to_date = new QDateEdit();
    to_date->setCalendarPopup(true);

    QLabel *pair = new QLabel(tr("Currency Pair"));
    QLabel *lfrom = new QLabel(tr("From"));
    QLabel *lto = new QLabel(tr("to"));
    QLabel *tf = new QLabel(tr("Time Frame"));

    QVBoxLayout *vl = new QVBoxLayout;

    vl->addWidget(pair);
    vl->addWidget(pairs);
    vl->addWidget(lfrom);
    vl->addWidget(from_date);
    vl->addWidget(lto);
    vl->addWidget(to_date);
    vl->addWidget(tf);
    vl->addWidget(timeframes);
    vl->addStretch(1);
    setLayout(vl);

    connect(from_date, SIGNAL(dateChanged(const QDate &)), this, SLOT(fromDateChanged(const QDate &)));
}

void MainTab::fromDateChanged(const QDate &date)
{
    to_date->setMinimumDate(date);
    to_date->calendarWidget()->setMinimumDate(date);
}
