import QtQuick
import QtQuick.Window
import QtWebEngine

Window {
    width: 1024
    height: 768
    visible: true
    WebEngineView {
        anchors.fill: parent
        url: "https://streetvoice.com/megafeihong"
    }
}
