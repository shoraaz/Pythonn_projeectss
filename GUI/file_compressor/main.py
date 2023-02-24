import PySimpleGUI as p
import makezip
label1 = p.Text("Select files to compress:-")
input1 = p.Input()
btn1 = p.FilesBrowse("Select", key="files")
label2 = p.Text("Select destination folder:-")
input2 = p.Input()
btn2 = p.FolderBrowse("Select", key="folder")
btn3 = p.Button("Compress")
output = p.Text(key="output")
window = p.Window("FILE COMPRESSOR",
                  layout=[[label1, input1, btn1],
                          [label2, input2, btn2],
                          [btn3, output]])
while True:
    event, values = window.read()
    #print(event,values)
    filepaths = values['files'].split(";")
    print(type(filepaths))
    folder = values["folder"]
    makezip.make_archive(filepaths,folder)
    window["output"].update("Files compressed successfully")

window.close()
