import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import hello.signals.greeter 1.0

ApplicationWindow {
  visible: true
  width: 800
  height: 600
  title: "Hello QtQuick"
  property int counter: 0

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
    anchors.margins: 5

    Pane {
      Layout.fillHeight: true
      Layout.fillWidth: true

      Text {
        id: greeting
        anchors.centerIn: parent

        text: "Hello World"
        font.pixelSize: 40
      }
    }

    RowLayout {
      Layout.fillWidth: true

      Item {
        Layout.fillWidth: true
      }
      Label {
        id: label1
        text: "Count:"
      }
      Label {
        text: counter.toString()
      }
    }

    Button {
      Layout.fillWidth: true
      text: "Click me!"
      onClicked: function() {
        counter += 1
        greeting.text = greeter.random()
      }
    }
  }
}
