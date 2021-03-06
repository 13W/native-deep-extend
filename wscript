# http://www.freehackers.org/~tnagy/wafbook/index.html
def set_options(opt):
  opt.tool_options("compiler_cxx")

def configure(conf):
  conf.check_tool("compiler_cxx")
  conf.check_tool("node_addon")
  conf.env.append_unique('CXXFLAGS', ['-Wall', '-O'])

def build(bld):
  ext = bld.new_task_gen("cxx", "shlib", "node_addon")
  ext.cxxflags = ["-I./src/", "-g", "-Wall"]
  ext.source = "./src/extend.cc"
  ext.target = "extend"
