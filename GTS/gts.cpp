#include "gts.h"
#include "ui_gts.h"

GTS::GTS(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::GTS)
{
    ui->setupUi(this);
}

GTS::~GTS()
{
    delete ui;
}
