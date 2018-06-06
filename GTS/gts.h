#ifndef GTS_H
#define GTS_H

#include <QMainWindow>

namespace Ui {
class GTS;
}

class GTS : public QMainWindow
{
    Q_OBJECT

public:
    explicit GTS(QWidget *parent = 0);
    ~GTS();

private:
    Ui::GTS *ui;
};

#endif // GTS_H
