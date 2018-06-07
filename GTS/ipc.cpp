#include "ipc.h"

IPC& IPC::getInstance()
{
    static IPC inst;
    return inst;
}

IPC::IPC(QWidget *parent):QDialog(parent)
{
    socket = new QUdpSocket(this);
    socket->bind(QHostAddress::LocalHost,IPC_SOCK);
    connect(socket,SIGNAL(readyRead()),this,SLOT(ReceiveData()));
}

quint64 IPC::SendData(QByteArray Data)
{
    qDebug()<<Data;
    return socket->writeDatagram(Data,QHostAddress::LocalHost,IPC_SOCK);
}

void IPC::ReceiveData()
{

    QByteArray Buffer;
     Buffer.resize(socket->pendingDatagramSize());

    QHostAddress sender;
    quint16 senderPort;
    socket->readDatagram(Buffer.data(),Buffer.size(),&sender,&senderPort);
    qDebug() << tr("IPC receive:") << Buffer.data();

}
