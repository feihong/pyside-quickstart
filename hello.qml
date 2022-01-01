import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import hello.signals.greeter 1.0

ApplicationWindow {
  visible: true
  width: 800
  height: 600
  title: "Hello QtQuick"
  property string greeting: "Hello World"

  Greeter {
    id: greeter
  }

  Shortcut {
    sequence: StandardKey.Quit
    context: Qt.ApplicationShortcut
    onActivated: Qt.quit()
  }

  ColumnLayout {
    anchors.fill: parent

    Rectangle {
      Layout.fillHeight: true
      Layout.fillWidth: true
      color: "transparent"

      Text {
        anchors.centerIn: parent

        text: greeting
        font.pixelSize: 40
      }
    }

    Button {
      Layout.fillWidth: true
      text: "Click me!"
      onClicked: greeting = greeter.random()
    }
  }
}
