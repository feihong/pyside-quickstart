import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
  visible: true
  width: 800
  height: 600
  title: "Hello QtQuick"
  property string greeting: "Hello World"

  ColumnLayout {
    anchors.fill: parent

    Rectangle {
      Layout.fillHeight: true
      Layout.fillWidth: true

      Text {
        anchors.centerIn: parent

        text: greeting
        font.pixelSize: 40
      }
    }

    Button {
      Layout.fillWidth: true
      text: "Click me!"
    }
  }
}