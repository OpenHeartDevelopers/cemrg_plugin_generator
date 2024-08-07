project(kcl_cemrgapp_myplugin)

mitk_create_plugin(
  EXPORT_DIRECTIVE MYPLUGIN
  EXPORTED_INCLUDE_SUFFIXES src
  MODULE_DEPENDS MitkQtWidgetsExt
)
