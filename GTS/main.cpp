#include "gts.h"
#include "maingui.h"
#include "ipc.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    MainGUI m_gui;
    m_gui.show();

    return a.exec();
}
