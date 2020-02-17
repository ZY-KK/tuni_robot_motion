/****************************************************************************
** Meta object code from reading C++ file 'marker_detection_display.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.5.1)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../src/marker_rviz_plugin/include/marker_detection/marker_detection_display.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'marker_detection_display.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.5.1. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
struct qt_meta_stringdata_marker_rviz_plugin__MarkerDetectionDisplay_t {
    QByteArrayData data[3];
    char stringdata0[57];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_marker_rviz_plugin__MarkerDetectionDisplay_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_marker_rviz_plugin__MarkerDetectionDisplay_t qt_meta_stringdata_marker_rviz_plugin__MarkerDetectionDisplay = {
    {
QT_MOC_LITERAL(0, 0, 42), // "marker_rviz_plugin::MarkerDet..."
QT_MOC_LITERAL(1, 43, 12), // "updateVisual"
QT_MOC_LITERAL(2, 56, 0) // ""

    },
    "marker_rviz_plugin::MarkerDetectionDisplay\0"
    "updateVisual\0"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_marker_rviz_plugin__MarkerDetectionDisplay[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
       1,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    0,   19,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void,

       0        // eod
};

void marker_rviz_plugin::MarkerDetectionDisplay::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        MarkerDetectionDisplay *_t = static_cast<MarkerDetectionDisplay *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->updateVisual(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObject marker_rviz_plugin::MarkerDetectionDisplay::staticMetaObject = {
    { &rviz::MessageFilterDisplay<marker_msgs::MarkerDetection>::staticMetaObject, qt_meta_stringdata_marker_rviz_plugin__MarkerDetectionDisplay.data,
      qt_meta_data_marker_rviz_plugin__MarkerDetectionDisplay,  qt_static_metacall, Q_NULLPTR, Q_NULLPTR}
};


const QMetaObject *marker_rviz_plugin::MarkerDetectionDisplay::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *marker_rviz_plugin::MarkerDetectionDisplay::qt_metacast(const char *_clname)
{
    if (!_clname) return Q_NULLPTR;
    if (!strcmp(_clname, qt_meta_stringdata_marker_rviz_plugin__MarkerDetectionDisplay.stringdata0))
        return static_cast<void*>(const_cast< MarkerDetectionDisplay*>(this));
    return rviz::MessageFilterDisplay<marker_msgs::MarkerDetection>::qt_metacast(_clname);
}

int marker_rviz_plugin::MarkerDetectionDisplay::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = rviz::MessageFilterDisplay<marker_msgs::MarkerDetection>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 1)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 1;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
