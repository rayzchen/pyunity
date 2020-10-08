#ifndef UNITY_H_
#define UNITY_H_

#include <string>
#include <vector>

class Tag;
class GameObject;
class Component;
class Transform;

class Tag {
    public:
        std::string tagName;
        std::string tag;
        Tag(std::string tagName);
        Tag(int tagNum);
};

class GameObject {
	public:
		char name[20];
        std::vector<Component> components;
		Transform* transform;
		GameObject(const char name[]);
		GameObject(const char name[], GameObject* parent);
        template <class T> T* AddComponent();
};

class Component {
	public:
		GameObject* gameObject;
		Transform* transform;
};

class Transform : Component {
	public:
		GameObject* gameObject;
		Transform* parent;
		Transform(Transform* parent);
};

#endif