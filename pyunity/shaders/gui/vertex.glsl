#version 330 core
layout (location = 0) in vec2 aPos;

uniform mat4 projection;
uniform mat4 model;
uniform float depth = 0.0;

out vec2 TexCoord;
out vec3 FragPos;

void main() {
    gl_Position = projection * model * vec4(aPos, depth, 0.5);
    TexCoord = aPos;
}
