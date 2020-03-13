load("@com_google_api_codegen//rules_gapic:gapic.bzl", "proto_custom_library")

def py_gapic_library2(name, srcs, **kwargs):
#    srcjar_target_name = "%s_srcjar" % name
    srcjar_target_name = name
    srcjar_output_suffix = ".srcjar"

    proto_custom_library(
        name = srcjar_target_name,
        deps = srcs,
        plugin = Label("@gapic_generator_python//:gapic_generator_python"),
        plugin_args = [],
        plugin_file_args = {},
        output_type = "python_gapic",
        output_suffix = srcjar_output_suffix,
        **kwargs
    )

