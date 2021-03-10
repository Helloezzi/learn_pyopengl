from OpenGL.GL.ARB import shader_atomic_counters
import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np

vertex_src = """
# version 330

layout(location = 0) in vec3 a_position;
layout(location = 1) in vec3 a_color;

out vec3 v_color;

void main()
{
    gl_Position = vec4(a_position, 1.0);
    v_color = a_color;
}
"""

fragment_src = """
# version 330

in vec3 v_color;
out vec4 out_color;

void main()
{
    out_color = vec4(v_color, 1.0);
}
"""

def window_resize(window, width, height):
    glViewport(0, 0, width, height)

if not glfw.init():
    raise Exception("glfw can not be initialized!")

window = glfw.create_window(1280, 720, "My Opengl window", None, None)

if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created")

glfw.set_window_pos(window, 400, 200)
glfw.set_window_size_callback(window, window_resize)
glfw.make_context_current(window)

"""
 vertices = [-0.5, -0.5, 0.0,
            0.5, -0.5, 0.0,
            0.0,  0.5, 0.0,
            1.0, 0.0, 0.0,
            0.0, 1.0, 0.0,
            0.0, 0.0, 1.0]
"""

vertices = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
            -0.5,  0.5, 0.0, 0.0, 0.0, 1.0,
            0.5, 0.5, 0.0, 1.0, 1.0, 1.0]

vertices = np.array(vertices, dtype=np.float32)
# colors = np.array(colors, dtype=np.float32)

shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

# position = glGetAttribLocation(shader, "a_position")
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

# color = glGetAttribLocation(shader, "a_color")
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

glUseProgram(shader)
glClearColor(0.5, 0.5, 0.5, 1)

while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT)

    glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

    glfw.swap_buffers(window)

glfw.terminate()
