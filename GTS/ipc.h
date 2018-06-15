#ifndef IPC_H
#define IPC_H
#include <QDialog>
#include <QUdpSocket>

#define IPC_RCV_SOCK    5867
#define IPC_SND_SOCK    5868
class IPC : public QDialog
{
    Q_OBJECT

    public:
    static IPC& getInstance();
        quint64 SendData(QByteArray Data);

    private:
        IPC(QWidget *parent = 0);
        IPC(IPC const&);
        void operator=(IPC const&);
        QUdpSocket *socket;

    signals:

    public slots:
        void ReceiveData();
};

#endif // IPC_H
