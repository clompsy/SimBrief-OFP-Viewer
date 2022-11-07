# SimBrief-OFP-Viewer
 Small Flask application server that allows viewing a simbrief OFP data.
 Additionally offers an update of the METARs from vatsim.

## Dependencies
 Uses Python Flask server to conveniently allow opening a website from any browser on the network to see the OFP data.
 Uses bootstrap 5.2 for UI components and bootstrap-dark theme (https://vinorodrigues.github.io/bootstrap-dark-5/)

## Running
 Install Python and run the simbrief_ofp_viewer.py
 Then open the URL in your browser either by specifying the simbrief ID or username:
 - http://localhost:5000/?id=999999
 - http://localhost:5000/?name=myname

## Packaging
 To create a standalone executable, package it using pyinstaller:
 pyinstaller --onefile simbrief_ofp_viewer.py --add-data="templates/*;templates/"