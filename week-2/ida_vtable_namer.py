import idc
import ida_ida
import idautils

# utility functions

def ida__get_min_ea():
   return ida_ida.inf_get_min_ea()
   
def ida__get_max_ea():
   return ida_ida.inf_get_max_ea()

def ida__demangle_name(name):
   return idc.demangle_name(name, idc.get_inf_attr(idc.INF_SHORT_DN))

def ida__get_name(ea):
   return idc.get_name(ea)

def ida__set_name(ea, name):
   idc.set_name(ea, name, SN_CHECK)

def ida__has_user_name(ea):
   return idc.hasUserName(ida_bytes.get_full_flags(ea))

def ida__get_qword(ea):
   return idc.get_qword(ea)

def ida__get_disasm(ea):
   return idc.GetDisasm(ea)

def ida__next_head(ea):
   return idc.next_head(ea)

def ida__segments():
   return idautils.Segments()
   
def ida__get_segment_name(segment):
   return idc.get_segm_name(segment)

# program functions

def is_non_templated_vtable(ea):
   name = ida__get_name(ea)
   if not name.startswith("??_7"):
       return False
       
   if "?" in name[4:]:
       return False
   
   return True
   
def is_valid_vtable_function(name, disasm):
   invalid_substrings = ["??", "off_"]
   return not any(substring in name for substring in invalid_substrings) and disasm.startswith("dq offset")

def name_vtable_methods(ea):
   class_name = ida__get_name(ea)
   class_name = ida__demangle_name(class_name)

   if class_name.startswith("const "):
       class_name = class_name[6:]
   if class_name.endswith("`vftable'"):
       class_name = class_name[:-11]
       
   offset = 0
   disasm = ida__get_disasm(ea)
   name  = class_name
   
   while is_valid_vtable_function(name, disasm):
       to_name = ida__get_qword(ea)
       
       if not ida__has_user_name(to_name):
           ida__set_name(to_name, "{}::m{:04X}".format(class_name, offset))
           
       offset += 8
       ea    = ida__next_head(ea)
       disasm = ida__get_disasm(ea)
       name  = ida__get_name(ea)
   return ea

def name_vtables(begin:int = 0, end:int = 0):
   _begin = ida__get_min_ea()
   _end  = ida__get_max_ea()
   
   if begin != 0:
      _begin = begin
   if end != 0:
       _end = end
   
   for segment in ida__segments():
       if ida__get_segment_name(segment) != ".rdata":
           continue
       i = _begin
       while i < _end:
           if not is_non_templated_vtable(i):
               i += 1
               continue
           temp = i
           i = name_vtable_methods(i)
           if i == temp:
               i += 1
       
name_vtables()
