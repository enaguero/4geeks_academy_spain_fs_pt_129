[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 📋 Day 18: TodoList Application using React

## 🎯 Learning Objectives

This day will teach you to build a complete to-do list application in React, learning key concepts such as:

- **useEffect Hook**: Understand the lifecycle of functional components
- **Lifecycle**: How and when code runs at different moments
- **Combining Hooks**: Using useState + useEffect together
- **React Forms**: Creating and handling controlled inputs
- **Input Validation**: Validating user data naturally
- **React Hook Form**: Using professional libraries for complex forms
- **Event & event.target**: Understanding events in forms

## 📚 Day Structure

This day is organized into 6 incremental steps, each building on the previous one:

### Step 1: useEffect Basics ⚙️
**Folder**: `step1-useeffect-basico/`

You will learn what useEffect is, when it runs, and how to use it.

**Concepts**:
- What useEffect is
- The dependencies array
- Cleaning up effects (cleanup)

---

### Step 2: Component Lifecycle 🔄
**Folder**: `step2-ciclo-vida/`

You will understand when code runs during a component's life.

**Concepts**:
- Mounting
- Updating
- Unmounting

---

### Step 3: useState + useEffect 🔗
**Folder**: `step3-usestate-useeffect/`

You will combine both hooks to update the UI automatically.

**Concepts**:
- Syncing state with effects
- Avoiding infinite loops
- Re-rendering and effects

---

### Step 4: Basic Forms 📝
**Folder**: `step4-forms-basico/`

You will create your first React form with controlled inputs.

**Concepts**:
- Controlled inputs
- event.target.value
- onChange handlers
- Two-way data binding

---

### Step 5: Simple Validation ✅
**Folder**: `step5-validacion-simple/`

You will add manual input validation without external libraries.

**Concepts**:
- Validating inputs in real time
- Displaying error messages
- Preventing submission of invalid forms

---

### Step 6: React Hook Form 🚀
**Folder**: `step6-react-hook-form/`

You will use a professional library for complex forms.

**Concepts**:
- How React Hook Form works
- Registering inputs
- Automatic validation
- Error handling

---

## 🚀 How to Use This Material

### 1. Follow in order
Each step depends on the previous one. Don't skip steps.

### 2. Experiment
Modify the code, try new things, break it intentionally and fix it.

### 3. Practice
Each step has practical exercises. Do them!

### 4. Understand, don't memorize
Try to understand *why* it works, not just *how*.

## 📖 Recommended Reading

### From 4Geeks Academy
- [Controlled vs Uncontrolled Inputs in React](https://4geeks.com/lesson/controlled-vs-uncontrolled-inputs-react-js)

### Official React
- [useEffect Hook - React Docs](https://react.dev/reference/react/useEffect)
- [useState Hook - React Docs](https://react.dev/reference/react/useState)

### React Hook Form
- [Official documentation](https://react-hook-form.com/)

## 🎓 Final Project

**TodoList Application**

By the end of this day, you will build a complete to-do list application with:

✅ Add tasks  
✅ Mark tasks as completed  
✅ Delete tasks  
✅ Input validation  
✅ Local storage (localStorage)  
✅ Responsive interface  

## 💡 Important Tips

### For Beginners

1. **Read everything first**: Before writing code, read the tutorials
2. **Copy and understand**: Don't just copy the code, understand every line
3. **Write by hand**: If possible, type the code instead of copy/paste
4. **Experiment**: Change values, add console.logs, try things

### Key Concepts

- **Rendering**: React draws the UI based on state
- **State**: Data that changes in the component
- **Effects**: Code that runs at certain moments
- **Validation**: Making sure data is correct before using it

## ⚠️ Common Errors

### Error: "React Hook 'useState' is called in a loop"
**Cause**: Calling hooks conditionally  
**Fix**: Hooks must always be at the root of the component

### Error: "setState during render"
**Cause**: Calling setState directly in the component  
**Fix**: Use useEffect for side effects

### Error: "Too many re-renders"
**Cause**: An effect causing an infinite state update  
**Fix**: Add the correct dependencies to the dependency array

## 🆘 Need Help?

1. Read the tutorial step by step
2. Search the concept on Google
3. Ask in the official Slack channel
4. Review the "Common Errors" section

## 📊 Progress

Check off each step as you complete it:

- [ ] Step 1: useEffect Basics
- [ ] Step 2: Lifecycle
- [ ] Step 3: useState + useEffect
- [ ] Step 4: Basic Forms
- [ ] Step 5: Simple Validation
- [ ] Step 6: React Hook Form
- [ ] Final Project: TodoList

---

**Let's build! 💪**

Remember: every professional developer went through this. Take your time, practice a lot, and have fun learning.
