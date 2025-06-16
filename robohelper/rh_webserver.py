
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer, HTTPServer
import urllib.parse
import json

class RH_WebServer_Functions():

	core = None

	def __init__(self, core):

		self.core = core
		self.core.debugmsg(5, "__init__")

	def get(self, req):
		self.core.debugmsg(5, "get:", req)

		resp = RH_ResponseObject(self.core)
		self.core.debugmsg(5, "resp:", resp)

		try:
			parsed_path = urllib.parse.urlparse(req.path)
			self.core.debugmsg(5, "parsed_path:", parsed_path)
			if parsed_path.path == '/':
				resp = self.web_ui_page(req)

		except Exception as e:
			self.core.debugmsg(5, "Exception:", e)
			resp.httpcode = 500
			resp.message = str(e)

		return resp

	def post(self, req):
		self.core.debugmsg(5, "post:", req)

		resp = RH_ResponseObject(self.core)
		return resp

	def put(self, req):
		self.core.debugmsg(5, "put:", req)

		resp = RH_ResponseObject(self.core)
		return resp

	def delete(self, req):
		self.core.debugmsg(5, "delete:", req)

		resp = RH_ResponseObject(self.core)
		return resp

	def head(self, req):
		self.core.debugmsg(5, "head:", req)

		resp = RH_ResponseObject(self.core)
		return resp


	# Pah specific functions

	def web_ui_page(self, req):
		self.core.debugmsg(5, "web_ui_page:", req)

		resp = RH_ResponseObject(self.core)
		self.core.debugmsg(5, "resp:", resp)
		resp.httpcode = 200
		resp.message  = "<html>"
		resp.message += 	"<head>"
		resp.message += 	"<title>Robo Helper</title>"
		resp.message += 	"</head>"
		resp.message += 	"<body>"
		resp.message += 	"<h1>Robo Helper</h1>"
		resp.message += 	"</body>"
		resp.message += "</html>"

		return resp

class RH_ResponseObject():

	core = None
	httpcode = 404
	headers = []
	message = None

	def __init__(self, core):
		self.core = core
		if len(self.headers) < 1:
			self.headers.append(("Server", "Robo Helper v" + self.core.version))


# class RH_WebServer_Blah(BaseHTTPRequestHandler):
#
# 	def do_HEAD(self):
# 		self.core.debugmsg(7, " ")
# 		return
#
# 	def do_DELETE(self):
# 		self.core.debugmsg(7, " ")
# 		actionfound = False
# 		httpcode = 500
# 		try:
# 			parsed_path = urllib.parse.urlparse(self.path)
# 			message = '{"path":"'+str(parsed_path)+'", "message": "Unsupported method"}'
# 			self.core.debugmsg(8, "parsed_path:", parsed_path)
# 			patharr = parsed_path.path.split("/")
# 			self.core.debugmsg(8, "patharr:", patharr)
# 			if not actionfound and len(patharr) == 2:
# 				actionfound = True
# 				# delete table
# 				tablename = urllib.parse.unquote_plus(patharr[1])
# 				self.core.debugmsg(9, "tablename:", tablename)
#
# 				deltbl = core.table_delete(tablename)
#
# 				if deltbl:
# 					httpcode = 200
# 					message = '{"message": "table '+tablename+' deleted"}'
#
# 				else:
# 					httpcode = 404
# 					message = '{"message": "table '+tablename+' does not exists"}'
#
#
# 			if not actionfound and len(patharr) == 3:
# 				actionfound = True
# 				# delete column
# 				tablename = urllib.parse.unquote_plus(patharr[1])
# 				self.core.debugmsg(9, "tablename:", tablename)
# 				columnname = urllib.parse.unquote_plus(patharr[2])
# 				self.core.debugmsg(9, "columnname:", columnname)
#
# 				delcol = core.column_delete(tablename, columnname)
# 				if delcol:
# 					httpcode = 200
# 					message = '{"message": "column '+columnname+' deleted"}'
#
# 				else:
# 					httpcode = 404
# 					message = '{"message": "column '+columnname+' does not exists"}'
#
#
#
# 			if not actionfound and len(patharr) == 4:
# 				actionfound = True
# 				# delete column
# 				tablename = urllib.parse.unquote_plus(patharr[1])
# 				self.core.debugmsg(9, "tablename:", tablename)
# 				columnname = urllib.parse.unquote_plus(patharr[2])
# 				self.core.debugmsg(9, "columnname:", columnname)
# 				columnvalue = urllib.parse.unquote_plus(patharr[3])
# 				self.core.debugmsg(9, "columnvalue:", columnvalue)
#
# 				delcol = core.value_delete(tablename, columnname, columnvalue)
# 				if delcol:
# 					httpcode = 200
# 					message = '{"message": "value '+columnvalue+' deleted"}'
#
# 				else:
# 					httpcode = 404
# 					message = '{"message": "value '+columnvalue+' does not exists"}'
#
#
#
#
# 		except Exception as e:
# 			self.core.debugmsg(6, "do_DELETE:", e)
# 			httpcode = 500
# 			message = str(e)
# 		try:
# 			self.send_response(httpcode)
# 			self.send_header("Server", "Test Data Table v"+core.version)
# 			self.end_headers()
# 			self.wfile.write(bytes(message,"utf-8"))
# 		except BrokenPipeError as e:
# 			self.core.debugmsg(8, "Browser lost connection, probably closed by user")
# 		except Exception as e:
# 			self.core.debugmsg(6, "do_PUT:", e)
# 		return
#
# 	def do_PUT(self):
# 		self.core.debugmsg(7, " ")
# 		actionfound = False
# 		httpcode = 500
# 		try:
# 			parsed_path = urllib.parse.urlparse(self.path)
# 			message = '{"path":"'+str(parsed_path.path)+'", "message": "Unsupported method"}'
# 			self.core.debugmsg(8, "parsed_path:", parsed_path)
# 			patharr = parsed_path.path.split("/")
# 			self.core.debugmsg(8, "patharr:", patharr)
#
# 			if not actionfound and len(patharr) == 2:
# 				actionfound = True
# 				# create table
# 				tablename = urllib.parse.unquote_plus(patharr[1])
# 				self.core.debugmsg(9, "tablename:", tablename)
# 				if len(tablename)<1:
# 					httpcode = 406
# 					message = '{"message": "table name cannot be blank"}'
# 				else:
# 					tableid = core.table_exists(tablename)
# 					self.core.debugmsg(9, "tableid:", tableid)
# 					if tableid:
# 						httpcode = 200
# 						message = '{"message": "table '+tablename+' exists"}'
# 					else:
# 						tableid = core.table_create(tablename)
# 						self.core.debugmsg(9, "tableid:", tableid)
# 						if tableid:
# 							httpcode = 201
# 							message = '{"message": "table '+tablename+' created"}'
#
#
# 			if not actionfound and len(patharr) == 3:
# 				actionfound = True
# 				# create column
# 				tablename = urllib.parse.unquote_plus(patharr[1])
# 				self.core.debugmsg(9, "tablename:", tablename)
# 				columnname = urllib.parse.unquote_plus(patharr[2])
# 				self.core.debugmsg(9, "columnname:", columnname)
#
# 				if len(columnname)<1:
# 					httpcode = 406
# 					message = '{"message": "column name cannot be blank"}'
# 				else:
#
# 					columnid = core.column_exists(tablename, columnname)
# 					self.core.debugmsg(9, "columnid:", columnid)
# 					if columnid:
# 						httpcode = 200
# 						message = '{"message": "column '+columnname+' exists"}'
# 					else:
# 						columnid = core.column_create(tablename, columnname)
# 						self.core.debugmsg(9, "columnid:", columnid)
# 						if columnid:
# 							httpcode = 201
# 							message = '{"message": "column '+columnname+' created"}'
#
#
# 			if not actionfound and len(patharr) == 4:
# 				actionfound = True
# 				# append value to column
# 				tablename = urllib.parse.unquote_plus(patharr[1])
# 				self.core.debugmsg(9, "tablename:", tablename)
# 				columnname = urllib.parse.unquote_plus(patharr[2])
# 				self.core.debugmsg(9, "columnname:", columnname)
# 				columnvalue = urllib.parse.unquote_plus(patharr[3])
# 				self.core.debugmsg(9, "columnvalue:", columnvalue)
#
# 				valueid = core.value_create(tablename, columnname, columnvalue)
# 				self.core.debugmsg(9, "valueid:", valueid)
# 				if valueid:
# 					httpcode = 201
# 					message = '{"message": "value '+columnvalue+' added to column '+columnname+'"}'
#
#
# 			if not actionfound and len(patharr) == 5:
# 				actionfound = True
# 				# replace value by id?
# 				tablename = urllib.parse.unquote_plus(patharr[1])
# 				self.core.debugmsg(9, "tablename:", tablename)
# 				columnname = urllib.parse.unquote_plus(patharr[2])
# 				self.core.debugmsg(9, "columnname:", columnname)
# 				value_id = urllib.parse.unquote_plus(patharr[3])
# 				self.core.debugmsg(9, "value_id:", value_id)
# 				columnvalue = urllib.parse.unquote_plus(patharr[4])
# 				self.core.debugmsg(9, "columnvalue:", columnvalue)
#
# 				curr_id = core.value_exists(tablename, columnname, value_id)
# 				if curr_id:
# 					result = core.value_replace_byid(tablename, columnname, curr_id, columnvalue)
# 					if result:
# 						httpcode = 200
# 						message = '{"message": "value id:'+value_id+' replaced with value:'+columnvalue+' in column '+columnname+'"}'
# 					else:
# 						httpcode = 501
# 						message = '{"message": "An unknown error occoured replaceing '+value_id+' with '+columnvalue+' in column '+columnname+'"}'
#
# 				else:
# 					httpcode = 404
# 					message = '{"message": "the value/id ('+value_id+') you are trying to replace doesn\'t exist"}'
#
#
#
#
# 		except Exception as e:
# 			self.core.debugmsg(6, "do_PUT:", e)
# 			httpcode = 500
# 			message = str(e)
#
# 		try:
# 			self.send_response(httpcode)
# 			self.send_header("Server", "Test Data Table v"+core.version)
# 			self.end_headers()
# 			self.wfile.write(bytes(message,"utf-8"))
# 		except BrokenPipeError as e:
# 			self.core.debugmsg(8, "Browser lost connection, probably closed by user")
# 		except Exception as e:
# 			self.core.debugmsg(6, "do_PUT:", e)
#
# 		return
#
# 	def do_POST(self):
# 		self.core.debugmsg(7, " ")
# 		actionfound = False
# 		httpcode = 500
# 		try:
# 			parsed_path = urllib.parse.urlparse(self.path)
# 			message = '{"path":"'+str(parsed_path.path)+'", "message": "Unsupported method"}'
# 			self.core.debugmsg(8, "parsed_path:", parsed_path)
# 			patharr = parsed_path.path.split("/")
# 			self.core.debugmsg(8, "patharr:", patharr)
#
# 			content_len = int(self.headers.get('Content-Length'))
# 			self.core.debugmsg(8, "content_len:", content_len)
# 			post_body = self.rfile.read(content_len)
# 			self.core.debugmsg(8, "post_body:", post_body)
#
# 			if not actionfound and len(patharr) == 3:
# 				# create column
# 				tablename = urllib.parse.unquote_plus(patharr[1])
# 				self.core.debugmsg(9, "tablename:", tablename)
# 				columnname = urllib.parse.unquote_plus(patharr[2])
# 				self.core.debugmsg(9, "columnname:", columnname)
#
# 				if columnname == "row":
# 					actionfound = True
# 					tableid = core.table_exists(tablename)
# 					self.core.debugmsg(9, "tableid:", tableid)
# 					if tableid:
# 						# now parse the post data and check all the columns exist
# 						#
# 						data = json.loads(post_body)
# 						self.core.debugmsg(9, "data:", data)
# 						for col in data.keys():
# 							result = core.value_create(tablename, col, data[col])
# 							self.core.debugmsg(9, "result:", result)
# 							if not result:
# 								httpcode = 500
# 								message = '{"message": "unable to put value '+data[col]+' into column '+col+' of table '+tablename+'"}'
#
# 						httpcode = 201
# 						message = '{"message": "values added to table: '+tablename+'"}'
#
# 					else:
# 						httpcode = 404
# 						message = '{"message": "table '+tablename+' not found"}'
#
#
# 				if columnname == "papaparse":
# 					actionfound = True
# 					data = json.loads(post_body)
# 					self.core.debugmsg(9, "data:", data)
# 					for row in data:
# 						self.core.debugmsg(9, "row:", row)
# 						for val in row:
# 							self.core.debugmsg(9, "val:", val)
# 							core.value_create(tablename, val, row[val])
#
# 					httpcode = 201
# 					message = '{"message": "values added to table: '+tablename+'"}'
#
#
# 		except Exception as e:
# 			self.core.debugmsg(6, "Exception:", e)
# 			httpcode = 500
# 			message = str(e)
#
# 		try:
# 			self.send_response(httpcode)
# 			self.send_header("Server", "Test Data Table v"+core.version)
# 			self.end_headers()
# 			self.wfile.write(bytes(message,"utf-8"))
# 		except BrokenPipeError as e:
# 			self.core.debugmsg(8, "Browser lost connection, probably closed by user")
# 		except Exception as e:
# 			self.core.debugmsg(6, "do_PUT:", e)
# 		return
#
# 	def do_GET(self):
#
# 		print("self.path:", self.path)
# 		print("self.request:", self.request)
# 		print("self.client_address:", self.client_address)
# 		print("self.server:", self.server)
# 		# print("self.path:", self.path)
#
# 		RH_WebServer_Core.core.debugmsg(5, "do_GET")
# 		httpcode = 200
# 		pathok = False
# 		try:
# 			parsed_path = urllib.parse.urlparse(self.path)
# 			self.core.debugmsg(8, "parsed_path:", parsed_path)
# 			if parsed_path.path == '/':
# 				pathok = True
# 				message  = "<html>"
# 				message += "<head>"
#
# 				# https://developers.google.com/speed/libraries#jquery-ui
# 				# Jquery
#
#
#
#
# 				message += "<script src=\""+core.config['Resources']['js_jquery']+"\"></script>"
# 				# Jquery UI
# 				message += "<link rel=\"stylesheet\" href=\""+core.config['Resources']['css_jqueryui']+"\">"
# 				message += "<script src=\""+core.config['Resources']['js_jqueryui']+"\"></script>"
#
# 				message += "<script src=\""+core.config['Resources']['js_papaparse']+"\"></script>"
#
# 				message += """	<style>
# 								.ui-tabs .ui-tabs-panel {
# 									padding: 0em 0em;
# 								}
#
# 								.tableFixHead          { overflow-y: auto; height: 88%; }
# 								.tableFixHead thead    { position: sticky; top: 0; width: 100%;}
# 								.tableFixHead thead th { position: sticky; top: 0; }
# 								/* .tableFixHead thead th span { float: left; } */
# 								.tableFixHead thead th span { float: left; padding-top: 5px; }
# 								.tableFixHead thead th span.ui-icon-close { position: absolute; top: 5px; right: 0px; }
#
# 								th, td { padding: 5px 10px; }
#
# 								.data-cell { min-width: 3em; }
# 								.has-value { background: #fff !important; }
#
# 								.ui-col-count { position: absolute; top: -5px; font-size: 0.7em; right: 20px; font-weight: normal; }
#
# 								#dialog-progress .ui-dialog-titlebar { display:none; }
# 								.progress-label { position: absolute; left: 40%; top: 28px; font-weight: bold; text-shadow: 1px 1px 0 #fff; }
# 								.ui-progressbar .ui-progressbar-value { height: 20px; }
#
# 								.ui-dialog { max-width: 90%; }
#
# 								</style> """
#
#
# 				message += "<script>"
# 				message += "var refreshinterval = 0;"
# 				message += "var refreshrunning = false;"
# 				# message += "var chunksize = 1048576;" # 1Mb
# 				message += "var chunksize = 1024*10;" # 1Mb
# 				message += "var chunkprocessed = 0;" # 1Mb
# 				message += "$(function() {"
# 				message += "	var tabs = $(\"#tables\" ).tabs();"
#
# 				message += "	$( \"#buttonbar\" ).controlgroup();"
# 				message += "	refresh();"
#
#
#
# 				message += "	dlgNewTable = $( \"#dialog-new-table\" ).dialog({"
# 				message += "		autoOpen: false,"
# 				message += "		height: \"auto\","
# 				message += "		width: \"auto\","
# 				message += "		modal: true,"
# 				message += "		buttons: {"
# 				message += "			Create: function() {"
# 				message += "				var tblname = $('#table-name').val();"
# 				message += "				console.log(\"#table-name: \" + $('#table-name'));"
# 				message += "				console.log(\"tblname: \" + tblname);"
# 				message += "				$.ajax({"
# 				message += "					url: '/'+tblname,"
# 				message += "					type: 'PUT',"
# 				message += "					dataType: 'json',"
# 				message += "					success: function(data) {"
# 				message += "						refresh();"
# 				message += "						setTimeout(function(){"
# 				message += "							$(\"li a:last\").trigger(\"click\");"
# 				message += "						}, 500);"
# 				message += "					}"
# 				message += "				});"
# 				message += "				$( this ).dialog( \"close\" );"
# 				message += "			},"
# 				message += "			Cancel: function() {"
# 				message += "				$( this ).dialog( \"close\" );"
# 				message += "			}"
# 				message += "		}"
# 				message += "	});"
#
# 				message += """ $('#table-name').keypress(function(e) {
# 									if (e.keyCode == $.ui.keyCode.ENTER) {
# 										var tblname = $('#table-name').val();
# 										console.log(\"#table-name: \" + $('#table-name'));
# 										console.log(\"tblname: \" + tblname);
# 										$.ajax({
# 											url: '/'+tblname,
# 											type: 'PUT',
# 											dataType: 'json',
# 											success: function(data) {
# 												refresh();
# 												setTimeout(function(){
# 													$("li a:last").trigger("click");
# 												}, 500);
#
# 											}
# 										});
# 										$( \"#dialog-new-table\" ).dialog( \"close\" );
# 									}
# 								}); """
#
#
# 				message += "	dlgDelTable = $( \"#dialog-delete-table\" ).dialog({"
# 				message += "		autoOpen: false,"
# 				message += "		height: \"auto\","
# 				message += "		width: \"auto\","
# 				message += "		modal: true,"
# 				message += "		buttons: {"
# 				message += "			Delete: function() {"
# 				message += "				tblname = $(\"#delete-table-name\").text();"
# 				message += "				console.log(\"tblname: \"+tblname);"
# 				message += "				$.ajax({"
# 				message += "					url: '/'+tblname,"
# 				message += "					type: 'DELETE',"
# 				message += "					dataType: 'json',"
# 				message += "					success: function(data) {"
# 				message += "						refresh();"
# 				message += "					}"
# 				message += "				});"
# 				message += "				$( this ).dialog( \"close\" );"
# 				message += "			},"
# 				message += "			Cancel: function() {"
# 				message += "				$( this ).dialog( \"close\" );"
# 				message += "			}"
# 				message += "		}"
# 				message += "	});"
#
# 				message += "	dlgAddColumn = $( \"#dialog-add-column\" ).dialog({"
# 				message += "		autoOpen: false,"
# 				message += "		height: \"auto\","
# 				message += "		width: \"auto\","
# 				message += "		modal: true,"
# 				message += "		buttons: {"
# 				message += "			Add: function() {"
# 				message += "				console.log(\"#column-name: \" + $('#column-name'));"
# 				message += "				var colname = $('#column-name').val();"
# 				message += "				console.log(\"colname: \" + colname);"
# 				message += "				var tblname = $('#column-table-name').text();"
# 				message += "				console.log(\"tblname: \" + tblname);"
# 				message += "				$.ajax({"
# 				message += "					url: '/'+tblname+'/'+colname,"
# 				message += "					type: 'PUT',"
# 				message += "					dataType: 'json',"
# 				message += "					success: function(data) {"
# 				message += "						refresh();"
# 				message += "					}"
# 				message += "				});"
# 				message += "				$( this ).dialog( \"close\" );"
# 				message += "			},"
# 				message += "			Cancel: function() {"
# 				message += "				$( this ).dialog( \"close\" );"
# 				message += "			}"
# 				message += "		}"
# 				message += "	});"
#
# 				message += """ $('#column-name').keypress(function(e) {
# 									if (e.keyCode == $.ui.keyCode.ENTER) {
# 										console.log(\"#column-name: \" + $('#column-name'));
# 										var colname = $('#column-name').val();
# 										console.log(\"colname: \" + colname);
# 										var tblname = $('#column-table-name').text();
# 										console.log(\"tblname: \" + tblname);
# 										$.ajax({
# 											url: '/'+tblname+'/'+colname,
# 											type: 'PUT',
# 											dataType: 'json',
# 											success: function(data) {
# 												refresh();
# 											}
# 										});
# 										$( \"#dialog-add-column\" ).dialog( \"close\" );
# 									}
# 								}); """
#
# 				# dialog-delete-column
# 				message += "	dlgDelColumn = $( \"#dialog-delete-column\" ).dialog({"
# 				message += "		autoOpen: false,"
# 				message += "		height: \"auto\","
# 				message += "		width: \"auto\","
# 				message += "		modal: true,"
# 				message += "		buttons: {"
# 				message += "			Delete: function() {"
# 				message += "				tblname = $(\"#delete-column-table\").text();"
# 				message += "				colname = $(\"#delete-column-name\").text();"
# 				message += "				console.log(\"tblname: \"+tblname);"
# 				message += "				$.ajax({"
# 				message += "					url: '/'+tblname+'/'+colname,"
# 				message += "					type: 'DELETE',"
# 				message += "					dataType: 'json',"
# 				message += "					success: function(data) {"
# 				message += "						var colhead = $('div[name=\"'+tblname+'\"]').find('th[name=\"'+colname+'\"]');"
# 				message += "						var colno = colhead.attr('colno');"
# 				message += "						colhead.remove();"
# 				message += "						$('td[colno=\"'+colno+'\"]').remove();"
# 				# message += "						refresh_table(tblname);"
# 				message += "						setTimeout(function(){"
# 				message += "							refresh_table(tblname);"
# 				message += "						}, 100);"
# 				message += "					}"
# 				message += "				});"
# 				message += "				$( this ).dialog( \"close\" );"
# 				message += "			},"
# 				message += "			Cancel: function() {"
# 				message += "				$( this ).dialog( \"close\" );"
# 				message += "			}"
# 				message += "		}"
# 				message += "	});"
#
#
# 				message += "	dlgProgress = $( \"#dialog-progress\" ).dialog({"
# 				message += "		autoOpen: false,"
# 				# message += "		classes: {\"no-close\": },"
# 				message += "		height: \"auto\","
# 				message += "		width: \"auto\","
# 				message += "		modal: false,"
# 				message += "	});"
#
# 				message += """	var progressbar = $("#dialog-progress").progressbar({
# 									value: false
# 								}); """
#
#
# 				message += """	dlgFileImport = $( \"#dialog-file-import\" ).dialog({
# 									autoOpen: false,
# 									height: \"auto\",
# 									width: \"auto\",
# 									modal: true,
# 									buttons: {
# 										Import: function() {
# 											$( this ).dialog( \"close\" );
# 											file_import_action();
# 										},
# 										Cancel: function() {
# 											$( this ).dialog( \"close\" );
# 										}
# 									}
# 								});"""
#
# 				# dialog-file-export
# 				message += """	dlgFileExport = $( \"#dialog-file-export\" ).dialog({
# 									autoOpen: false,
# 									height: \"auto\",
# 									width: \"auto\",
# 									modal: true,
# 									buttons: {
# 										Save: function() {
# 											/* $("#dialog-file-export output").css("display", "");
# 											$("#dialog-file-export output a").trigger("click"); */
# 											var a = document.getElementById("dialog-file-export").querySelector("output").querySelector("a");
# 											console.log("a:",a);
# 											a.click();
# 											$( this ).dialog( \"close\" );
# 											/* file_import_action(); */
# 										},
# 										Cancel: function() {
# 											$( this ).dialog( \"close\" );
# 										}
# 									}
# 								});"""
#
#
#
# 				message += "	tabs.on( \"click\", \"li span.ui-icon-close\", function() {"
# 				message += "		console.log( $( this ) );"
# 				message += "		console.log( $( this ).attr(\"table\") );"
# 				message += "		$(\"#delete-table-name\").text($( this ).attr(\"table\"));"
# 				message += "		dlgDelTable.dialog( \"open\" );"
# 				message += "	});"
#
# 				message += "	tabs.on( \"click\", \"th span.ui-icon-close\", function() {"
# 				message += "		console.log( $( this ) );"
# 				message += "		var tabactive = $( \"#tables\" ).tabs( \"option\", \"active\" );"
# 				message += "		console.log('tabactive:'+tabactive);"
# 				message += "		var tblname = $(\"#tables ul li:nth-child(\"+(tabactive+1)+\") a \").text();"
# 				message += "		console.log(\"tblname: \"+tblname);"
# 				message += "		var colname = $( this ).attr(\"column\");"
# 				message += "		console.log('colname: '+colname);"
# 				message += "		$(\"#delete-column-table\").text(tblname);"
# 				message += "		$(\"#delete-column-name\").text(colname);"
# 				message += "		dlgDelColumn.dialog( \"open\" );"
# 				message += "	});"
#
# 				message += "	tabs.on( \"click\", \"li.ui-tabs-tab\", function() {"
# 				message += "		console.log( $( this ) );"
# 				message += "		var tablename = $( this ).find('a').text();"
# 				message += "		console.log('tablename: '+tablename);"
# 				message += "		refreshrunning = false;"
# 				message += "		refresh_table(tablename);"
# 				message += "	});"
#
#
# 				message += "	$( \"#new-table\" ).button().on( \"click\", function() {"
# 				message += "		$('#table-name').val('');"
# 				message += "		dlgNewTable.dialog( \"open\" );"
# 				message += "	});"
#
# 				message += "	$( \"#new-column\" ).button().on( \"click\", function() {"
# 				message += "		var tabactive = $( \"#tables\" ).tabs( \"option\", \"active\" );"
# 				message += "		console.log('tabactive:'+tabactive);"
# 				message += "		var tblname = $(\"#tables ul li:nth-child(\"+(tabactive+1)+\") a \").text();"
# 				message += "		console.log(\"tblname: \"+tblname);"
# 				message += "		$(\"#column-table-name\").text(tblname);"
# 				message += "		$('#column-name').val('');"
# 				message += "		dlgAddColumn.dialog( \"open\" );"
# 				message += "	});"
#
# 				message += "	$( \"#import-file\" ).button().on( \"click\", function() {"
# 				message += "		$( \"#dialog-file-import-file\" ).val("");"
# 				message += "		dlgFileImport.dialog( \"open\" );"
# 				message += "	});"
#
# 				message += """	$( \"#export-file\" ).button().on( \"click\", function() {
# 									$('#export-file-table-name').val('');
# 									var active = $( "#tables" ).tabs( "option", "active" );
# 									console.log("active: " + active);
# 									var activetbl = $("#tables ul li:nth-child("+(active+1)+") a ").text();
# 									$('#export-file-table-name').val(activetbl);
# 									$("#dialog-file-export output").css("display", "None");
# 									dlgFileExport.dialog( \"open\" );
# 									file_export_preview();
# 								});"""
#
#
#
# 				message += "	$( \"#refresh\" ).button().on( \"click\", function() {"
# 				message += "		refresh();"
# 				message += "	});"
#
# 				message += "	$( \"#help\" ).button().on( \"click\", function() {"
# 				message += "		window.open(\"https://github.com/damies13/TestDataTable/blob/master/Doc/rest_api.md#rest-api\");"
# 				message += "	});"
#
# 				message += "	$( \"#auto-refresh\" ).on( \"selectmenuchange\", function() {"
# 				message += "		console.log(\"#auto-refresh:	this:\"+this);"
# 				message += "		refreshinterval = this.value;"
# 				message += "		auto_refresh(this.value);"
# 				message += "	});"
#
#
#
# 				# dialog-file-import-file
# 				message += "	$( \"#dialog-file-import-file\" ).on( \"change\", function() {"
# 				message += "		console.log(\"#dialog-file-import-file:	this:\"+this);"
# 				message += "		file_import_preview();"
# 				message += "	});"
# 				# dialog-file-import-delimiter
# 				message += "	$( \"#dialog-file-import-delimiter\" ).on( \"change\", function() {"
# 				message += "		console.log(\"#dialog-file-import-delimiter:	this:\"+this);"
# 				message += "		file_import_preview();"
# 				message += "	});"
# 				# dialog-file-import-header-row
# 				message += "	$( \"#dialog-file-import-header-row\" ).on( \"change\", function() {"
# 				message += "		console.log(\"#dialog-file-import-header-row:	this:\"+this);"
# 				message += "		file_import_preview();"
# 				message += "	});"
# 				# dialog-file-import-encoding
# 				message += "	$( \"#dialog-file-import-encoding\" ).on( \"change\", function() {"
# 				message += "		console.log(\"#dialog-file-import-encoding:	this:\"+this);"
# 				message += "		file_import_preview();"
# 				message += "	});"
# 				# dialog-file-import-comments
# 				message += "	$( \"#dialog-file-import-comments\" ).on( \"change\", function() {"
# 				message += "		console.log(\"#dialog-file-import-comments:	this:\"+this);"
# 				message += "		file_import_preview();"
# 				message += "	});"
#
#
# 				# dialog-file-export-file
# 				message += "	$( \"#dialog-file-export-file\" ).on( \"change\", function() {"
# 				message += "		console.log(\"#dialog-file-export-file:	this:\"+this);"
# 				message += "		file_export_preview();"
# 				message += "	});"
# 				# dialog-file-export-delimiter
# 				message += "	$( \"#dialog-file-export-delimiter\" ).on( \"change\", function() {"
# 				message += "		console.log(\"#dialog-file-export-delimiter:	this:\"+this);"
# 				message += "		file_export_preview();"
# 				message += "	});"
# 				# dialog-file-export-header-row
# 				message += "	$( \"#dialog-file-export-header-row\" ).on( \"change\", function() {"
# 				message += "		console.log(\"#dialog-file-export-header-row:	this:\"+this);"
# 				message += "		file_export_preview();"
# 				message += "	});"
#
#
# 				message += "});"
#
# 				message += """	function auto_refresh(value) {
# 									console.log("auto_refresh:	refreshinterval:"+refreshinterval);
# 									console.log("auto_refresh:	value:"+value);
# 									if (refreshinterval == value && value>0){
# 										setTimeout(function(){
# 											auto_refresh(value);
# 										}, value*1000);
# 										refresh();
# 									}
# 								};"""
#
#
# 				message += "function refresh() {"
# 				message += "	$.getJSON('tables', function(tables) { "
# 				message += "		refresh_tables(tables);"
# 				message += "	});"
# 				message += "};"
#
# 				message += """	function refresh_tables(tables) {
# 									var keeptables = [];
# 									for (var i = 0; i < tables.tables.length; i++) {
# 										console.log(tables.tables[i]);
# 										var tableid = tables.tables[i].tbl_id;
# 										var tablenme = tables.tables[i].table;
# 										var tabid = tableid.toString() +'_'+ tablenme.split(' ').join('_');
# 										keeptables.push(tabid);
# 										console.log("tabid: " + tabid);
# 										console.log($("[href='#"+tabid+"']").length);
# 										if (!$("[href='#"+tabid+"']").length){
# 											$("#tables").append('<div id="' + tabid + '" name="'+tablenme+'"  class=\"tableFixHead\"></div>');
# 											$("#tables ul").append('<li><a href="#' + tabid + '">'
# 												+ tablenme
# 												+ '</a> <span class="ui-icon ui-icon-close" role="presentation" table="'
# 												+ tablenme + '">Remove Tab</span></li>');
# 											$( "#tables" ).tabs( "refresh" );
# 										}
# 									}
# 									console.log("keeptables: " + keeptables);
# 									console.log($("#tables ul li").length);
# 									for (var i = 0; i < $("#tables ul li").length; i++) {
# 										console.log($("#tables ul li")[i]);
# 										var thistbl = $("#tables ul li:nth-child("+(i+1)+") a ").attr("href");
# 										thistbl = thistbl.substr(1);
# 										console.log("thistbl: "+thistbl);
# 										if (!keeptables.includes(thistbl)){
# 											console.log("remove thistbl: "+thistbl);
# 											$("#tables ul li:nth-child("+(i+1)+")").remove();
# 										}
# 									}
# 									var active = $( "#tables" ).tabs( "option", "active" );
# 									console.log("active: " + active);
# 									if (!active) {
# 										$( "#tables" ).tabs( "option", "active", 0 );
# 									}
# 									var active = $( "#tables" ).tabs( "option", "active" );
# 									console.log("active: " + active);
# 									var activetbl = $("#tables ul li:nth-child("+(active+1)+") a ").text();
# 									if (activetbl.length <1){
# 										active = 0;
# 										console.log("active: " + active);
# 										var activetbl = $("#tables ul li:nth-child("+(active+1)+") a ").trigger("click");
# 									} else {
# 										console.log("activetbl: "+activetbl);
# 										refresh_table(activetbl);
# 									}
#
# 								};"""
#
# 				message += """	function refresh_table(tablename) {
# 									if (!refreshrunning){
# 										refreshrunning = true;
# 										console.log("refresh_table: tablename:"+tablename);
# 										$.getJSON(tablename, function(tabledata) {
# 											refresh_table_data(tabledata);
# 										});
# 									}
# 								};"""
#
# 				message += """	function refresh_table_data(tabledata) {
# 									console.log("refresh_table_data_new: tabledata:", tabledata);
# 									var tbl_name = Object.keys(tabledata)[0];
# 									console.log("tbl_name: "+tbl_name);
# 									/* ensure columns */
# 									var tblid = $('div[name="'+tbl_name+'"]').attr('id');
# 									console.log("tblid: "+tblid);
# 									console.log($('div[name="'+tbl_name+'"] table').length);
# 									if (!$('div[name="'+tbl_name+'"] table').length){
# 										// console.log($('div[name="'+tbl_name+'"]'));
# 										$('div[name="'+tbl_name+'"]').append('<table id=\"table-'+tblid+'\"><thead><tr><th class="ui-widget-header">Row</th></tr></thead><tbody></tbody></table>');
# 									}
# 									var safecols = [];
# 									for (var i = 0; i < tabledata[tbl_name].length; i++) {
# 										var col_name = tabledata[tbl_name][i]["column"];
# 										console.log("col_name: "+col_name);
# 										var col_id = tabledata[tbl_name][i]["col_id"];
# 										var colno = tblid+'-'+col_id;
# 										console.log("colno: "+colno);
# 										safecols.push(colno);
# 										if (!$('table[id="table-'+tblid+'"] thead tr th[colno="'+colno+'"]').length){
# 											$('table[id="table-'+tblid+'"] thead tr').append('<th class="ui-widget-header" id="'+col_id+'" name="'+col_name+'" colno="'+colno+'"><span column="'+col_name+'" class="ui-icon ui-icon-close" role="presentation">Remove Column</span><span>'+col_name+'</span><span class="ui-col-count">(0)</span></div></th>');
# 										}
# 									}
# 									console.log("safecols: ",safecols);
# 									/* remove columns that no longer exist on the server */
# 									var dispcols = $('table[id="table-'+tblid+'"] thead tr th');
# 									console.log("dispcols: ",dispcols);
# 									for (var i = 0; i < dispcols.length; i++) {
# 										console.log("dispcols["+i+"]: ",dispcols[i]);
# 										var thiscolno = $(dispcols[i]).attr('colno');
# 										console.log("thiscolno: ",thiscolno);
# 										if (thiscolno && safecols.indexOf(thiscolno) < 0){
# 											/* remove column */
# 											console.log("remove thiscolno: ",thiscolno);
# 											$('th[colno=\"'+thiscolno+'\"]').remove();
# 											$('td[colno=\"'+thiscolno+'\"]').remove();
# 										}
# 									}
#
# 									/* start populating rows */
# 									refresh_table_data_row(0, tabledata);
# 								};"""
#
# 				message += """	function refresh_table_data_row(rt_row, tabledata) {
# 									console.log("refresh_table_data_row: rt_row: "+rt_row);
# 									/* console.log("refresh_table_data_row: rt_row: "+rt_row+"	tabledata:", tabledata); */
# 									var tbl_name = Object.keys(tabledata)[0];
# 									/* console.log("tbl_name: "+tbl_name); */
# 									var tblid = $('div[name="'+tbl_name+'"]').attr('id');
# 									/* console.log("tblid: "+tblid); */
#
#
# 									var tabactive = $( "#tables" ).tabs( "option", "active" );
# 									/* console.log('tabactive:'+tabactive); */
# 									var tabactivename = $("#tables ul li:nth-child("+(tabactive+1)+") a ").text();
# 									/* console.log("tabactive: "+tabactive); */
#
# 									if (tbl_name == tabactivename){
#
# 										/* ensure row exists */
# 										if (!$('div[name="'+tbl_name+'"] table tbody tr[id="'+rt_row+'"]').length){
# 											console.log('Insert rt_row: '+rt_row);
# 											$('div[name="'+tbl_name+'"] table tbody').append('<tr id="'+rt_row+'"><td class="ui-widget-header">'+(rt_row+1)+'</td></tr>');
# 										}
#
# 										var maxcount = 0;
# 										for (var k = 0; k < tabledata[tbl_name].length; k++) {
# 											/* ensure cells exists */
# 											var kcol_id = tabledata[tbl_name][k]['col_id'];
# 											if (!$('div[name="'+tbl_name+'"] table tbody tr[id="'+rt_row+'"] td[id="'+kcol_id+'-'+rt_row+'"]').length){
# 												/* console.log('Insert cell: '+kcol_id+'-'+rt_row); */
# 												$('div[name="'+tbl_name+'"] table tbody tr[id="'+rt_row+'"]').append('<td id="'+kcol_id+'-'+rt_row+'" val_id="" class="data-cell ui-state-default" colno="'+tblid+'-'+kcol_id+'">&nbsp;</td>');
# 												$('div[name="'+tbl_name+'"] table tbody tr[id="'+rt_row+'"] td[id="'+kcol_id+'-'+rt_row+'"]').on( "click", function() {
# 													table_cell_clicked($( this ));
# 												});
# 											}
#
# 											/* update column count */
# 											count = tabledata[tbl_name][k]["values"].length;
# 											/* console.log("count: "+count); */
# 											$('th[id="'+kcol_id+'"] span[class="ui-col-count"]').text("("+count+")");
# 											if (count>maxcount){
# 												maxcount = count
# 											}
#
# 											/* populate cell data */
# 											if (rt_row < count){
#
# 												editcell = $('div[name="'+tbl_name+'"]').find('#'+kcol_id+'-'+rt_row);
# 												if (!editcell.is("[currval]")){
#
# 													var value = tabledata[tbl_name][k]["values"][rt_row]["value"];
# 													var val_id = tabledata[tbl_name][k]["values"][rt_row]["val_id"];
# 													/* console.log("val_id: "+val_id+'  value: '+value); */
#
# 													editcell.empty();
# 													editcell.text(value);
# 													editcell.attr("val_id", val_id);
# 													if (!editcell.hasClass("has-value")){ editcell.toggleClass("has-value"); }
# 												}
# 											} else {
# 												/* depopulate cell data (ensure empty) */
# 												editcell = $('div[name="'+tbl_name+'"]').find('#'+kcol_id+'-'+rt_row);
# 												if (!editcell.is("[currval]")){
# 													editcell.empty();
# 													editcell.html("&nbsp;");
# 													editcell.attr("val_id", "");
# 													if (editcell.hasClass("has-value")){ editcell.toggleClass("has-value"); }
# 												}
#
# 											}
#
# 										}
#
# 										/* keep going? */
# 										if (rt_row < maxcount + 4) {
# 											var delay = 1;
# 											setTimeout(function(){
# 												refresh_table_data_row(rt_row+1, tabledata);
# 											}, delay);
# 										} else {
# 											refreshrunning = false;
# 											$("tr").filter(function() {
# 												return parseInt($(this).attr("id")) > (maxcount+4);
# 											}).remove();
# 										}
#
# 									}
#
# 								};"""
#
#
#
# 				# /* click to edit data values */
# 				message += """	function table_cell_clicked(cell) {
# 									console.log('td cell on click:');
# 									console.log(cell);
# 									console.log(cell.is("[lastclicked]"));
# 									if (cell.is("[lastclicked]")){
# 										console.log(cell.attr('lastclicked'));
# 										var lastclicked = cell.attr('lastclicked');
# 										console.log('lastclicked: '+lastclicked);
# 										var timediff = Date.now() - Number(lastclicked);
# 										console.log('timediff: '+timediff);
# 										if (timediff>300 && timediff<2000) {
# 											// enter edit mode
# 											var currval = "";
# 											if (cell.hasClass("has-value")){
# 												currval = cell.text();
# 											}
# 											console.log('currval: '+currval);
# 											cell.attr('currval', currval);
# 											cell.empty();
# 											cell.append("<input type='text' id='editcell'>");
# 											var inputfield = cell.find("#editcell");
# 											inputfield.val(currval);
# 											inputfield.focus();
# 											cell.removeAttr("lastclicked");
# 										} else {
# 											$("td[lastclicked]").removeAttr("lastclicked");
# 										}
#
# 									} else {
# 										// check if cell has input feild, if so do nothing
# 										if (!cell.find("#editcell").length){
# 											// next check if another cell has input feild, if so do end edit
# 											if ($("td[currval]").length){
# 												// exit cell edit
# 												var editcell = $("td[currval]");
# 												var prevval = editcell.attr("currval");
# 												var newval = editcell.find("#editcell").val();
# 												console.log('prevval: '+prevval+'	newval:'+newval);
# 												if (prevval != newval){
# 													// update cell value
#
# 													var val_id = editcell.attr("val_id");
# 													console.log('val_id: '+val_id);
#
# 													var colno = editcell.attr("colno");
# 													console.log('colno: '+colno);
# 													var columnname = $("th[colno='"+colno+"']").attr("name");
# 													console.log('columnname: '+columnname);
#
# 													var tbl_id = colno.split("-")[0];
# 													console.log('tbl_id: '+tbl_id);
# 													var tablename = $("#"+tbl_id).attr("name");
# 													console.log('tablename: '+tablename);
#
# 													var puturl = "";
# 													var resttype = 'PUT';
# 													if (val_id.length>0){
# 														if (newval.length<1){
# 															resttype = 'DELETE';
# 															puturl = "/"+tablename+"/"+columnname+"/"+val_id;
# 														} else {
# 															puturl = "/"+tablename+"/"+columnname+"/"+val_id+"/"+newval;
# 														}
# 													} else {
# 														puturl = "/"+tablename+"/"+columnname+"/"+newval;
# 													}
# 													console.log('resttype: '+resttype+'	puturl: '+puturl);
# 													$.ajax({
# 														url: puturl,
# 														type: resttype,
# 														dataType: 'json',
# 														success: function(data) {
# 															refresh();
# 														}
# 													});
#
# 												}
# 												editcell.empty();
# 												if (newval.length<1){
# 													editcell.html("&nbsp;");
# 													editcell.attr("val_id", "");
# 												} else {
# 													editcell.text(newval);
# 												}
# 												editcell.removeAttr("currval");
# 											}
# 											$("td[lastclicked]").removeAttr("lastclicked");
# 											cell.attr("lastclicked", Date.now());
#
# 										}
# 									}
#
#
# 								};"""
#
# 				message += """	function file_import_preview() {
# 									console.log("file_import_preview:");
# 									var file = $("#dialog-file-import-file").val();
# 									console.log("file_import_preview: file: "+file);
# 									var delim = $("#dialog-file-import-delimiter").val();
# 									console.log("file_import_preview: delim: '"+delim+"'");
# 									var hrow = $("#dialog-file-import-header-row").prop("checked");
# 									console.log("file_import_preview: hrow: "+hrow);
# 									var encd = $("#dialog-file-import-encoding").val();
# 									console.log("file_import_preview: encd: "+encd);
# 									var scmt = $("#dialog-file-import-comments").val();
# 									console.log("file_import_preview: scmt: "+scmt);
#
# 									if (scmt.length<1){
# 										scmt = false;
# 										console.log("file_import_preview: scmt: "+scmt);
# 									}
#
# 									console.log("file_import_preview: file obj: ");
# 									console.log($("#dialog-file-import-file")[0]['files'][0]);
#
# 									var config = {
# 										delimiter: delim,
# 										header: hrow,
# 										encoding: encd,
# 										comments: scmt,
# 										preview: 5,
# 										skipEmptyLines: true,
# 										complete: function(results) {
# 											console.log("Finished:", results.data);
# 											var keys = Object.keys(results.data[0])
# 											console.log(keys);
# 											console.log("file_import_preview: hrow: "+hrow);
# 											r = 0;
# 											$("#dialog-file-import-preview table").html("<tr id='preview-tablerow-"+r+"'></tr>");
# 											/* do columns */
# 											i = 0;
#
# 											var rowtemplate = `<tr id='preview-tablerow-zzrowzz'>`;
# 											for (var key in keys) {
# 												$("#preview-tablerow-"+r+"").append("<th class=\\"ui-widget-header\\"><input id=\\"preview-c"+i+"\\" type=\\"text\\" size=\\"10\\"></th>");
# 												console.log("#preview-c"+i+":", keys[key]);
# 												$("#preview-c"+i).val(keys[key]);
# 												rowtemplate += `<td id='preview-tablecell-zzrowzz-${i}' class=\\"data-cell ui-state-default\\">&nbsp;</td>`;
#
# 												i++;
# 											}
# 											rowtemplate += `</tr>`;
# 											console.log("rowtemplate:", rowtemplate);
#
# 											for (var row in results.data) {
# 												var rowdata = results.data[row];
# 												r++;
# 												/* $("#dialog-file-import-preview table").append("<tr id='preview-tablerow-"+r+"'></tr>"); */
# 												$("#dialog-file-import-preview table").append(rowtemplate.replace(/zzrowzz/g, r));
# 												console.log("rowtemplate:", rowtemplate.replace(/zzrowzz/g, r));
#
# 												i = 0;
# 												for (var key in rowdata) {
# 													/* $("#preview-tablerow-"+r+"").append("<td class=\\"ui-widget-header\\"><input id=\\"preview-c"+i+"\\" type=\\"text\\" size=\\"10\\"></th>"); */
# 													$("#preview-tablecell-"+r+"-"+i).text(rowdata[key].trim());
# 													i++;
# 												}
# 											}
# 										}
# 									}
#
#
#
# 									Papa.parse($("#dialog-file-import-file")[0]['files'][0], config);
#
# 								};"""
#
# 				# <tr><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><tr>
#
#
# 				# dialog-file-import-file
# 				# dialog-file-import-delimiter
# 				# dialog-file-import-header-row
# 				# dialog-file-import-encoding
# 				# dialog-file-import-comments
# 				message += """	function file_import_action() {
# 									console.log("file_import_action:");
# 									var file = $("#dialog-file-import-file").val();
# 									console.log("file_import_preview: file: "+file);
# 									var delim = $("#dialog-file-import-delimiter").val();
# 									console.log("file_import_preview: delim: '"+delim+"'");
# 									var hrow = $("#dialog-file-import-header-row").prop("checked");
# 									console.log("file_import_preview: hrow: "+hrow);
# 									var encd = $("#dialog-file-import-encoding").val();
# 									console.log("file_import_preview: encd: "+encd);
# 									var scmt = $("#dialog-file-import-comments").val();
# 									console.log("file_import_preview: scmt: "+scmt);
#
# 									if (scmt.length<1){
# 										scmt = false;
# 										console.log("file_import_preview: scmt: "+scmt);
# 									}
#
# 									console.log("file_import_preview: file obj: ");
# 									console.log($("#dialog-file-import-file")[0]['files'][0]);
#
# 									var size = $("#dialog-file-import-file")[0]['files'][0]['size'];
# 									console.log("file_import_preview: size: "+size);
#
# 									var tabactive = $( "#tables" ).tabs( "option", "active" );
# 									console.log('tabactive:'+tabactive);
# 									var tblname = $("#tables ul li:nth-child("+(tabactive+1)+") a ").text();
# 									console.log("tblname: "+tblname);
#
# 									/* 	# dialog-progress
# 										#  <div id="dialog-progress-bar"><div id="dialog-progress-msg"></div></div> */
# 									$("#dialog-progress-subject").text("Importing file: '"+$("#dialog-file-import-file")[0]['files'][0]['name']+"' into table: '"+tblname+"'");
# 									dlgProgress.dialog( \"open\" );
# 									$("#dialog-progress").css("min-height", "50px");
# 									$("#dialog-progress").prev().css("display","none");
# 									$("div[aria-describedby='dialog-progress']").css("top", "1%");
# 									$("div[aria-describedby='dialog-progress']").css("left", "1%");
# 									dlgProgressMsg = $("#dialog-progress-msg")
# 									dlgProgressMsg.text("Loading....");
#
# 									var colheads = $("#preview-tablerow-0 th input");
# 									console.log("file_import_preview: colheads: ",colheads);
# 									var columns = [];
# 									var col_name = "";
# 									for (var colno=0; colno<colheads.length; colno++){
# 										console.log("file_import_preview: colno: "+colno+"	colheads[colno]:", colheads[colno]);
# 										col_name = colheads[colno]['value'].trim();
# 										columns.push(col_name);
# 										/* PUT /<table name>/<column name> */
#
# 										var puturl = "/"+tblname+"/"+col_name;
# 										console.log("puturl:", puturl);
# 										$.ajax({
# 											url: puturl,
# 											dataType: 'text',
# 											type: 'put',
# 											success: function( data, textStatus, jQxhr ){
# 												console.log("Created col_name:", col_name);
# 											}
# 										});
#
# 									}
# 									console.log("columns: ", columns);
# 									var progresssize = 0;
# 									chunkprocessed = 0;
#
# 									var chunkInCount = 0;
# 									var chunkOutCount = 0;
#
# 									var config = {
# 										delimiter: delim,
# 										header: hrow,
# 										encoding: encd,
# 										comments: scmt,
# 										skipEmptyLines: true,
# 										worker: false,
# 										beforeFirstChunk: function(chunk) {
# 											var index = chunk.match( /\\r\\n|\\r|\\n/ ).index;
# 											var headings = chunk.substr(0, index).split( delim );
# 											for (var colno=0; colno<columns.length; colno++){
# 												headings[colno] = columns[colno];
# 											}
# 											return headings.join() + chunk.substr(index);
# 										},
# 										chunkSize: chunksize,
# 										chunk: function(results) {
# 											console.log("chunk:", results);
# 											console.log("chunk: data:", results.data);
#
# 											var posturl = "/"+tblname+"/papaparse";
# 											console.log("posturl:", posturl);
#
# 											var stbldata = JSON.stringify(results.data);
# 											console.log("stbldata:", stbldata);
#
# 											chunkInCount++;
# 											console.log("chunkInCount:", chunkInCount);
#
# 											$.ajax({
# 												url: posturl,
# 												dataType: 'text',
# 												type: 'post',
# 												data: stbldata,
# 												success: function( data, textStatus, jQxhr ){
#
# 													progresssize += chunksize;
# 													var pcnt = Math.round(progresssize/size * 100);
# 													if (pcnt>100){
# 														pcnt = 100;
# 														lastrow = true;
# 													}
#
# 													dlgProgressMsg.text(pcnt+"%");
# 													$("#dialog-progress").progressbar( "value", pcnt );
# 													chunkOutCount++;
# 													console.log("chunkOutCount:", chunkOutCount);
# 													if (chunkInCount==chunkOutCount){
# 														close_file_import_progress();
# 													}
# 												}
# 											});
#
# 										}
# 									}
#
# 									Papa.parse($("#dialog-file-import-file")[0]['files'][0], config);
#
# 								};"""
#
# 				message += """	function close_file_import_progress() {
# 									dlgProgressMsg.text(100+"%");
# 									$("#dialog-progress").progressbar( "value", 100 );
# 									setTimeout(function(){
# 										dlgProgress.dialog( \"close\" );
# 									}, 500);
#
# 									var tabactive = $( "#tables" ).tabs( "option", "active" );
# 									var tblname = $("#tables ul li:nth-child("+(tabactive+1)+") a ").text();
# 									console.log("tblname: "+tblname);
# 									refresh_table(tblname);
# 								};"""
#
# 				message += """	function file_import_delimiter_tab() {
# 									console.log("file_import_delimiter_tab: '	'");
# 									$("#dialog-file-import-delimiter").val("	");
# 									file_import_preview();
# 								};"""
#
# 				message += """	function file_export_delimiter_tab() {
# 									console.log("file_export_delimiter_tab: '	'");
# 									$("#dialog-file-export-delimiter").val("	");
# 									file_export_preview();
# 								};"""
#
# 				message += """	function file_export_preview() {
# 									console.log("file_export_preview:");
# 									var table = $("#export-file-table-name").val();
# 									var delim = $("#dialog-file-export-delimiter").val();
# 									if (delim.length<1){
# 										delim = ",";
# 									}
#
# 									fileext = "";
# 									switch(delim) {
# 										case ",":
#   											fileext = ".csv";
# 											break;
# 										case "	":
#   											fileext = ".tsv";
# 											break;
# 										default:
#   											fileext = ".txt";
# 									}
# 									var d = new Date();
# 									var datestring = "_" + d.getFullYear() + ("0"+(d.getMonth()+1)).slice(-2) + ("0" + d.getDate()).slice(-2) + "_" + ("0" + d.getHours()).slice(-2) + ("0" + d.getMinutes()).slice(-2) + ("0" + d.getSeconds()).slice(-2);
# 									$("#dialog-file-export-filename").val(table + datestring + fileext);
# 									$("#dialog-file-export-preview textarea").val("loading table: "+table+" .......");
#
# 									var hrow = $("#dialog-file-export-header-row").prop("checked");
#
# 									var config = {
# 										delimiter: delim,
# 										header: hrow,
# 										skipEmptyLines: true
# 									}
#
# 									var geturl = "/"+table+"/papaparse";
# 									console.log("geturl:", geturl);
# 									$.ajax({
# 										url: geturl,
# 										success: function( data, textStatus, jQxhr ){
#
# 											window.URL = window.webkitURL || window.URL;
#
# 											console.log("data: ", data);
# 											$("#dialog-file-export-preview textarea").val("parseing table data: "+table+" .......");
# 											var text = Papa.unparse(data, config);
# 											$("#dialog-file-export-preview textarea").val(text);
#
# 											var output = $("#dialog-file-export output");
# 											var prevLink = $("#dialog-file-export output a");
# 											if (prevLink) {
# 												window.URL.revokeObjectURL(prevLink.href);
# 												$("#dialog-file-export output a").remove();
# 											}
#
# 											const MIME_TYPE = 'text/plain';
#   											var bb = new Blob([text], {type: MIME_TYPE});
#
# 											var a = document.createElement('a');
# 											a.download = $("#dialog-file-export-filename").val();
# 											a.href = window.URL.createObjectURL(bb);
# 											a.textContent = 'Download ready';
#
# 											a.dataset.downloadurl = [MIME_TYPE, a.download, a.href].join(':');
# 											output.append(a);
#
#
# 										}
# 									});
#
# 								};"""
#
#
#
# 				message += "</script>"
#
# 				message += "<style>"
# 				message += "#buttonbar { float: right; }"
# 				message += "#version   { float: left; font-size: 30%; }"
# 				message += "#title     { float: left; }"
# 				message += "</style>"
#
# 				message += "<title>Test Data Table</title>"
# 				message += "</head>"
# 				message += "<body>"
#
# 				#
# 				# Dialogues
# 				#
# 				message += "<div id=\"dialog-new-table\" title=\"Create table\">"
# 				message += "<div>Create a new table</div>"
# 				message += "  <label for='table-name'>Table Name:</label>"
# 				message += "  <input id='table-name' type='text'>"
# 				message += "</div>"
#
# 				message += "<div id=\"dialog-delete-table\" title=\"Delete table?\">"
# 				message += "<div>Are you sure you want to delete the table \""
# 				message += "<span id='delete-table-name'></span>"
# 				message += "\"?</div>"
# 				message += "</div>"
#
# 				message += "<div id=\"dialog-add-column\" title=\"Add Column\">"
# 				# column-table-name
# 				message += "<div>Add column to table \""
# 				message += "<span id='column-table-name'></span>"
# 				message += "\"</div>"
# 				message += "  <label for='column-name'>Column Name:</label>"
# 				message += "  <input id='column-name' type='text'>"
# 				message += "</div>"
#
# 				message += "<div id=\"dialog-delete-column\" title=\"Delete column?\">"
# 				message += "<div>Are you sure you want to delete the column \""
# 				message += "<span id='delete-column-name'></span>"
# 				message += "\" from table \"<span id='delete-column-table'></span>"
# 				message += "\"?</div>"
# 				message += "</div>"
#
#
# 				message += """	<div id="dialog-progress" title="Progress">
# 									<div id="dialog-progress-subject">Progress</div>
# 									<!-- <br /> -->
# 									<div id="dialog-progress-bar"><div id="dialog-progress-msg" class="progress-label"></div></div>
# 								</div>"""
#
# 				message += """	<div id="dialog-file-import" title="Text File Import">
# 									<table>
# 									<tr><td colspan="5">
# 										<label for='dialog-file-import-file'>Select File:</label>
# 										<input id='dialog-file-import-file' type='file'>
# 									</td></tr>
# 									<tr><td>
# 										<label for='dialog-file-import-delimiter'>File Delimiter:</label>
# 										<input id='dialog-file-import-delimiter' type='text' size='5' maxlength='1' placeholder='auto'>
# 										<a href="javascript:file_import_delimiter_tab();" id='dialog-file-import-insert-tab'>tab</a>
# 									</td><td>
# 										<label for='dialog-file-import-header-row'>Header Row:</label>
# 										<input id='dialog-file-import-header-row' type='checkbox' checked='true'>
# 									</td><td>
# 										<label for='dialog-file-import-encoding'>Encoding:</label>
# 										<input type="text" id="dialog-file-import-encoding" placeholder="default" size="7">
# 									</td><td>
# 										<label for='dialog-file-import-comments'>Comment char:</label>
# 										<input type="text" size="7" maxlength="10" placeholder="default" id="dialog-file-import-comments">
# 									</td></tr>
# 									</table>
# 									<br>
# 									<div>Preview:</div>
# 									<div id='dialog-file-import-preview' style="overflow-x: auto;">
# 										<table>
# 											<thead>
# 												<tr>
# 													<th class="ui-widget-header"><input id="preview-c1" type="text" value="Column 1" size="10"></th>
# 													<th class="ui-widget-header"><input id="preview-c2" type="text" value="Column 2" size="10"></th>
# 													<th class="ui-widget-header"><input id="preview-c3" type="text" value="Column 3" size="10"></th>
# 													<th class="ui-widget-header"><input id="preview-c4" type="text" value="Column 4" size="10"></th>
# 													<th class="ui-widget-header"><input id="preview-c5" type="text" value="Column 5" size="10"></th>
# 												<tr>
# 											</thead>
# 										<tbody>
# 											<tr><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><tr>
# 											<tr><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><tr>
# 											<tr><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><tr>
# 											<tr><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><tr>
# 											<tr><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><td class="data-cell ui-state-default">&nbsp;</td><tr>
# 										</tbody>
# 										</table>
# 									</div>
# 								</div>"""
#
# 				message += """	<div id="dialog-file-export" title="Text File Export">
# 									<table>
# 									<tr><td>
# 										<label for='dialog-file-export-delimiter'>File Delimiter:</label>
# 										<input id='dialog-file-export-delimiter' type='text' size='5' maxlength='1' placeholder='auto'>
# 										<a href="javascript:file_export_delimiter_tab();" id='dialog-file-export-insert-tab'>tab</a>
# 									</td><td>
# 										<label for='dialog-file-export-header-row'>Header Row:</label>
# 										<input id='dialog-file-export-header-row' type='checkbox' checked='true'>
# 									</td></tr>
# 									<tr><td colspan="5">
# 										<label for='dialog-file-export-filename'>Output File:</label>
# 										<input id='dialog-file-export-filename' type='text' size='60'>
# 									</td></tr>
# 									</table>
# 									<input id='export-file-table-name' type='hidden'>
# 									<br>
# 									<div>Preview:</div>
# 									<div id='dialog-file-export-preview' style="overflow-x: auto;">
# 									<textarea class='data-cell ui-state-default' disabled='' rows='6' cols='80' style='resize:none;'></textarea>
# 									</div>
# 									<output style="display: None;"></output>
# 								</div>"""
#
#
#
# 				#
# 				# Main page
# 				#
# 				#version font-size: 30%;
# 				# <fieldset>
# 				# message += "<div id=\"title\" class=\"ui-widget\">Test Data Table</div>"
# 				# message += "<div id=\"version\" class=\"ui-state-disabled ui-widget\">Version " + core.version + "</div>"
# 				message += "<div id=\"buttonbar\">"
# 				# message += "	<button>Test Data Table</button>" # spacer
# 				# message += "	<button disabled><span style=\"font-size: 30%;\">Version "+core.version+"</span>&nbsp;</button>"
# 				message += "	<button id='new-table' class=\"ui-button ui-widget ui-corner-all ui-button-icon-only\" title=\"Add Table\"><span class=\"ui-icon ui-icon-calculator\"></span>Add Table</button>"
# 				message += "	<button id='new-column' class=\"ui-button ui-widget ui-corner-all ui-button-icon-only\" title=\"Add Column\"><span class=\"ui-icon ui-icon-grip-solid-vertical\"></span>Add Column</button>"
# 				message += "	<button>&nbsp;</button>" # spacer
#
# 				message += """	<button id='import-file' class='ui-button ui-widget ui-corner-all ui-button-icon-only' title="Import File">
# 									<span class='ui-icon ui-icon-folder-open'></span>
# 									Import File</button> """
#
# 				message += """	<button id='export-file' class='ui-button ui-widget ui-corner-all ui-button-icon-only' title="Export File">
# 									<span class='ui-icon ui-icon-disk'></span>
# 									Export File</button> """
#
# 				message += "	<button>&nbsp;</button>" # spacer
# 				message += "	<select id='auto-refresh'>"
# 				message += "		<option value='0' >Auto Refresh Off</option>"
# 				message += "		<option value='5' >Auto Refresh 5 seconds</option>"
# 				message += "		<option value='10' >Auto Refresh 10 seconds</option>"
# 				message += "		<option value='30' >Auto Refresh 30 seconds</option>"
# 				message += "		<option value='60' >Auto Refresh 1 minute</option>"
# 				message += "	</select>"
# 				message += "	<button id='refresh' class=\"ui-button ui-widget ui-corner-all ui-button-icon-only\" title=\"Refresh\"><span class=\"ui-icon ui-icon-refresh\"></span>Refresh</button>"
# 				message += "	<button id='help' class=\"ui-button ui-widget ui-corner-all ui-button-icon-only\" title=\" Help\nv" + core.version + "\"><span class=\"ui-icon ui-icon-help\"></span>Help</button>"
# 				message += "</div>"
#
# 				message += "<div style=\"height: 5%;\">"
# 				message += "</div>"
#
# 				message += "<div id='tables'>"
# 				message += "<ul>"
# 				message += "</ul>"
# 				message += "</div>"
#
# 				message += "</body>"
# 				message += "</html>"
#
# 			self.core.debugmsg(8, "parsed_path:", parsed_path)
# 			filename, fileext = os.path.splitext(parsed_path.path)
# 			self.core.debugmsg(8, "fileext:", fileext)
# 			if not pathok and len(fileext)>0:
# 				localfile = "."+parsed_path.path
# 				self.core.debugmsg(8, "localfile:", localfile)
# 				self.core.debugmsg(8, "path.exists:", os.path.exists(localfile))
# 				if os.path.exists(localfile):
# 					pathok = True
# 					self.core.debugmsg(8, "pathok:", pathok)
#
# 					self.core.debugmsg(9, "httpcode:", httpcode)
# 					self.send_response(httpcode)
# 					self.send_header("Server", "Test Data Table v"+core.version)
# 					self.end_headers()
# 					with open(localfile,"rb") as f:
# 						self.core.debugmsg(8, "file open for read")
# 						self.wfile.write(f.read())
# 					return
#
#
# 			self.core.debugmsg(8, "parsed_path:", parsed_path)
# 			if not pathok and parsed_path.path == '/tables':
# 				pathok = True
# 				message = ""
# 				jsonresp = {}
# 				jsonresp["tables"] = core.tables_getall()
# 				message = json.dumps(jsonresp)
#
# 			self.core.debugmsg(8, "parsed_path:", parsed_path)
# 			patharr = parsed_path.path.split("/")
# 			self.core.debugmsg(8, "patharr:", patharr)
# 			if not pathok and len(patharr) == 2:
# 				tablename = urllib.parse.unquote_plus(patharr[1])
# 				self.core.debugmsg(9, "tablename:", tablename)
#
# 				tableid = core.table_exists(tablename)
# 				self.core.debugmsg(9, "tableid:", tableid)
# 				if tableid:
# 					pathok = True
# 					httpcode = 200
# 					jsonresp = {}
# 					jsonresp[tablename] = core.table_columns(tablename)
# 					i = 0
# 					for col in jsonresp[tablename]:
# 						self.core.debugmsg(9, "col:", col)
# 						jsonresp[tablename][i]["values"] = core.column_values(tablename, col["column"])
# 						i += 1
# 					message = json.dumps(jsonresp)
#
# 			if not pathok and len(patharr) == 3:
# 				tablename = urllib.parse.unquote_plus(patharr[1])
# 				self.core.debugmsg(9, "tablename:", tablename)
# 				columnname = urllib.parse.unquote_plus(patharr[2])
# 				self.core.debugmsg(6, "tablename:", tablename)
#
# 				if columnname == "papaparse":
# 					tableid = core.table_exists(tablename)
# 					self.core.debugmsg(9, "tableid:", tableid)
# 					if tableid:
# 						pathok = True
# 						httpcode = 200
#
# 						jsonresp = []
#
# 						columnnames = core.table_columns(tablename)
# 						i = 0
# 						for col in columnnames:
# 							self.core.debugmsg(9, "col:", col)
# 							columndata = core.column_values(tablename, col["column"])
# 							self.core.debugmsg(9, "columndata:", columndata)
# 							j = 0
# 							for val in columndata:
# 								self.core.debugmsg(9, "val:", val)
# 								self.core.debugmsg(9, "j:", j, "	len(jsonresp):",len(jsonresp))
# 								if len(jsonresp)-1 < j:
# 									newrow = {}
# 									self.core.debugmsg(9, "newrow:", newrow)
# 									jsonresp.append(newrow)
# 								jsonresp[j][col["column"]] = val['value']
# 								j += 1
#
# 							# self.core.debugmsg(9, "jsonresp:", jsonresp)
# 							i += 1
#
# 						message = json.dumps(jsonresp)
#
# 				if columnname == "columns":
# 					tableid = core.table_exists(tablename)
# 					self.core.debugmsg(9, "tableid:", tableid)
# 					if tableid:
# 						pathok = True
# 						httpcode = 200
#
# 						jsonresp = {}
# 						jsonresp[tablename] = core.table_columns(tablename)
#
# 						message = json.dumps(jsonresp)
#
# 				if columnname == "row":
# 					tableid = core.table_exists(tablename)
# 					self.core.debugmsg(9, "tableid:", tableid)
# 					if tableid:
# 						pathok = True
# 						httpcode = 200
#
# 						jsonresp = {}
# 						jsonresp[tablename] = {}
#
# 						columns = core.table_columns(tablename)
# 						self.core.debugmsg(9, "columns:", columns)
# 						for col in columns:
# 							self.core.debugmsg(9, "col:", col)
# 							column_name = col["column"]
# 							self.core.debugmsg(9, "column_name:", column_name)
# 							val_data = core.value_consume(tablename, column_name)
# 							self.core.debugmsg(9, "val_data:", val_data)
# 							if val_data is None:
# 								jsonresp[tablename][column_name] = None
# 							else:
# 								jsonresp[tablename][column_name] = val_data["value"]
#
# 						message = json.dumps(jsonresp)
#
#
# 				columnid = core.column_exists(tablename, columnname)
# 				self.core.debugmsg(6, "columnid:", columnid)
# 				if columnid:
# 					pathok = True
# 					httpcode = 200
# 					val_data = core.value_consume(tablename, columnname)
# 					if val_data is None:
# 						jsonresp = {columnname : None}
# 					else:
# 						jsonresp = {columnname : val_data["value"]}
# 					self.core.debugmsg(9, "jsonresp:", jsonresp)
# 					message = json.dumps(jsonresp)
#
#
# 				if columnname.isdigit():
# 					rownum = int(columnname)
# 					tableid = core.table_exists(tablename)
# 					self.core.debugmsg(8, "tableid:", tableid)
# 					if tableid:
# 						# pathok = True
# 						# httpcode = 200
#
# 						jsonresp = {}
# 						jsonresp[tablename] = {}
#
# 						columns = core.table_columns(tablename)
# 						self.core.debugmsg(8, "columns:", columns)
# 						for col in columns:
# 							self.core.debugmsg(8, "col:", col)
# 							column_name = col["column"]
# 							self.core.debugmsg(8, "column_name:", column_name)
# 							colvalues = core.column_values(tablename, column_name)
# 							self.core.debugmsg(8, "colvalues:", colvalues)
# 							self.core.debugmsg(8, "len(colvalues):", len(colvalues), "	rownum:", rownum)
# 							if len(colvalues) > rownum:
# 								pathok = True
# 								httpcode = 200
# 								valueid = colvalues[rownum]['val_id']
# 								self.core.debugmsg(8, "valueid:", valueid)
#
# 								data = core.value_consume_byid(tablename, column_name, valueid)
# 								if data is not None:
# 									jsonresp[tablename][column_name] = data["value"]
#
#
# 							else:
# 								jsonresp[tablename][column_name] = None
#
# 							# val_data = core.value_consume(tablename, column_name)
# 							# self.core.debugmsg(9, "val_data:", val_data)
# 							# if val_data is None:
# 							# 	jsonresp[tablename][column_name] = None
# 							# else:
# 							# 	jsonresp[tablename][column_name] = val_data["value"]
#
# 						message = json.dumps(jsonresp)
#
#
# 			if not pathok and len(patharr) == 4:
# 				tablename = urllib.parse.unquote_plus(patharr[1])
# 				self.core.debugmsg(9, "tablename:", tablename)
# 				columnname = urllib.parse.unquote_plus(patharr[2])
# 				self.core.debugmsg(9, "tablename:", tablename)
# 				columntype = urllib.parse.unquote_plus(patharr[3])
# 				self.core.debugmsg(9, "columntype:", columntype)
#
# 				if columntype == "all":
# 					pathok = True
# 					httpcode = 200
#
# 					jsonresp = {}
# 					jsonresp[columnname] = core.column_values(tablename, columnname)
#
# 					message = json.dumps(jsonresp)
#
# 				data = core.value_consume_byid(tablename, columnname, columntype)
# 				if data is not None:
# 					pathok = True
# 					httpcode = 200
# 					jsonresp = {}
# 					jsonresp[columnname] = data["value"]
# 					message = json.dumps(jsonresp)
#
#
# 			self.core.debugmsg(8, "parsed_path:", parsed_path)
# 			if not pathok:
# 				httpcode = 404
# 				self.core.debugmsg(9, "httpcode:", httpcode)
# 				message = None
# 				# message = "Unrecognised request: {}".format(parsed_path.path)
# 				# self.core.debugmsg(9, "message:", message)
# 		except Exception as e:
# 			self.core.debugmsg(6, "do_GET:", e)
# 			httpcode = 500
# 			message = str(e)
#
# 		try:
# 			self.core.debugmsg(9, "httpcode:", httpcode)
# 			self.send_response(httpcode)
# 			self.send_header("Server", "Test Data Table v"+core.version)
# 			self.end_headers()
# 			self.core.debugmsg(9, "message:", message)
# 			if message is not None:
# 				self.wfile.write(bytes(message,"utf-8"))
# 		except BrokenPipeError as e:
# 			self.core.debugmsg(8, "Browser lost connection, probably closed by user")
# 		except Exception as e:
# 			self.core.debugmsg(6, "do_PUT:", e)
#
# 		return
#
# 	def handle_http(self):
# 		self.core.debugmsg(7, " ")
# 		return
#
# 	def respond(self):
# 		self.core.debugmsg(7, " ")
# 		return
#
# 	# 	log_request is here to stop BaseHTTPRequestHandler logging to the console
# 	# 		https://stackoverflow.com/questions/10651052/how-to-quiet-simplehttpserver/10651257#10651257
# 	def log_request(self, code='-', size='-'):
# 		self.core.debugmsg(7, " ")
# 		pass
