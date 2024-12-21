#
# Copyright (C) 2023, Inria
# GRAPHDECO research group, https://team.inria.fr/graphdeco
# All rights reserved.
#
# This software is free for non-commercial, research and evaluation use
# under the terms of the LICENSE.md file.
#
# For inquiries contact  george.drettakis@inria.fr
#

from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension
import os

os.path.dirname(os.path.abspath(__file__))

setup(
    name="diff_gaussian_rasterization",
    packages=["diff_gaussian_rasterization"],
    ext_modules=[
        CUDAExtension(
            name="diff_gaussian_rasterization._C",
            sources=[
                "cuda_rasterizer/rasterizer_impl.cu",
                "cuda_rasterizer/forward.cu",
                "cuda_rasterizer/backward.cu",
                "cuda_rasterizer/apply_weights.cu",
                "rasterize_points.cu",
                "ext.cpp",
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "third_party/gl3w/src/gl3w.c"),
            ],
            # 安装eigen，glfw和gl3w后修改此处
            include_dirs=[
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "third_party/glm"),
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "third_party/eigen"),
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "third_party/gl3w/include"),
                '/usr/include'
                          ],
            library_dirs=['/usr/lib'],
            libraries=['GL'],
            extra_compile_args={
                "nvcc": [
                    "-I"
                    + os.path.join(
                        os.path.dirname(os.path.abspath(__file__)), "third_party/glm/")
                    # + os.path.join(
                    #     os.path.dirname(os.path.abspath(__file__)), "third_party/eigen/include")
                    # + os.path.join(
                    #     os.path.dirname(os.path.abspath(__file__)), "third_party/glew/glew-2.0.0/include")
                    + os.path.join(
                        os.path.dirname(os.path.abspath(__file__)), "third_party/gl3w/include")
                ]
            },
        )
    ],
    cmdclass={"build_ext": BuildExtension},
)
