[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 📞 Step 10: Contact List App Project

## 🎯 Goal

**YOUR PROJECT!** Build a complete contact management application applying **EVERYTHING** you learned in the previous steps:

- ✅ React Router (navigation)
- ✅ Context API (global state)
- ✅ useReducer (CRUD management)
- ✅ Controlled forms
- ✅ Validations
- ✅ Programmatic navigation

---

## ⚠️ IMPORTANT

**This step does NOT include a solved version.**

You'll only find:
- Project description
- Functional requirements
- Suggested structure
- Mockups/wireframes
- Documentation references

**YOU MUST IMPLEMENT IT** using what you learned in steps 1-9.

---

## 📋 Project Description

You'll build a **contact management application** where you can:
- View a list of all contacts
- Add a new contact
- View a contact's details
- Edit an existing contact
- Delete a contact (with confirmation)

All contacts will be managed with **global state** (Context + useReducer) and accessible from any page.

---

## 🎯 Required Features

### 1. Contact List (`/`)
- Show every contact in a list or cards
- Each contact displays: name, phone, email
- Buttons: "View detail", "Edit", "Delete"
- If there are no contacts, show a "No contacts" message
- "Add contact" button that navigates to `/add`

### 2. Add Contact (`/add`)
- Form with fields:
  - Name (required)
  - Phone (required)
  - Email (required, validate format)
  - Address (optional)
- Validations:
  - Don't leave required fields empty
  - Valid email
  - Phone numbers only
- On submit:
  - Add contact to global state
  - Navigate to `/` (list)
  - Show a success message
- "Cancel" button that returns to `/`

### 3. View Detail (`/contact/:id`)
- Show all contact information
- Buttons: "Edit", "Delete", "Back to list"
- If the ID doesn't exist, show "Contact not found" and a link to home

### 4. Edit Contact (`/edit/:id`)
- Form pre-filled with current data
- Same validations as Add
- On submit:
  - Update contact in global state
  - Navigate to the contact's detail
  - Show a success message
- "Cancel" button that returns to detail

### 5. Delete Contact
- Show confirmation: "Are you sure?"
- If confirmed:
  - Delete from global state
  - Navigate to `/` (list)
  - Show "Contact deleted" message
- If canceled, do nothing

### 6. Navbar
- Link to "Home" (contact list)
- Counter: "X contacts"
- "Add contact" link

### 7. 404 Page
- For routes that don't exist
- A friendly message
- Link back to home

---

## 🎨 Suggested Project Structure

```
contact-list-app/
├── src/
│   ├── context/
│   │   ├── ContactContext.js      # Context Provider + useReducer
│   │   └── contactReducer.js      # Reducer with CRUD actions
│   ├── pages/
│   │   ├── Home.js                # Contact list
│   │   ├── AddContact.js          # Add form
│   │   ├── EditContact.js         # Edit form
│   │   ├── ContactDetail.js       # View detail
│   │   └── NotFound.js            # 404 page
│   ├── components/
│   │   ├── Navbar.js              # Navigation
│   │   ├── ContactCard.js         # Contact card
│   │   ├── ContactForm.js         # Reusable form
│   │   └── ConfirmModal.js        # Confirmation modal
│   ├── App.js                     # Router and Providers
│   └── main.jsx                   # Entry point
```

---

## 🧠 Global State Structure

### Initial State

```javascript
const initialState = {
  contacts: [
    {
      id: 1,
      name: 'Juan Pérez',
      phone: '555-0101',
      email: 'juan@example.com',
      address: '123 Main Street'
    },
    {
      id: 2,
      name: 'María García',
      phone: '555-0102',
      email: 'maria@example.com',
      address: '456 Central Avenue'
    }
  ]
};
```

### Required Actions

```javascript
const CONTACT_ACTIONS = {
  ADD_CONTACT: 'ADD_CONTACT',
  UPDATE_CONTACT: 'UPDATE_CONTACT',
  DELETE_CONTACT: 'DELETE_CONTACT'
};
```

### Suggested Helper Functions

```javascript
// In ContactContext.js
const addContact = (contactData) => { ... };
const updateContact = (id, contactData) => { ... };
const deleteContact = (id) => { ... };
const getContactById = (id) => { ... };
```

---

## 🎨 Visual Mockup

```
┌─────────────────────────────────────────┐
│  [Navbar]  Home | Add | 3 contacts      │
├─────────────────────────────────────────┤
│                                         │
│  CONTACTS                               │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Juan Pérez                        │ │
│  │ 📞 555-0101  ✉️ juan@example.com  │ │
│  │ [View] [Edit] [Delete]            │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ María García                      │ │
│  │ 📞 555-0102  ✉️ maria@example.com │ │
│  │ [View] [Edit] [Delete]            │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [+ Add New Contact]                    │
│                                         │
└─────────────────────────────────────────┘
```

---

## ✅ Implementation Checklist

### Step 1: Initial Setup
- [ ] Create project with Vite
- [ ] Install react-router-dom
- [ ] Set up folder structure

### Step 2: Context and Reducer
- [ ] Create `contactReducer.js` with CRUD actions
- [ ] Create `ContactContext.js` with Provider
- [ ] Implement custom hook `useContacts()`
- [ ] Add initial sample data

### Step 3: Router
- [ ] Configure BrowserRouter in App.js
- [ ] Define every route
- [ ] Create basic page components

### Step 4: Contact List
- [ ] Display list from Context
- [ ] Create ContactCard component
- [ ] Implement delete button with confirmation
- [ ] Links to view detail and edit

### Step 5: Add Contact
- [ ] Create form with validations
- [ ] Wire up to addContact from Context
- [ ] Programmatic navigation after adding
- [ ] Success/error messages

### Step 6: View Detail
- [ ] Read the :id parameter from the URL
- [ ] Find contact by ID
- [ ] Show all the information
- [ ] Handle contact-not-found

### Step 7: Edit Contact
- [ ] Pre-fill form with current data
- [ ] Wire up to updateContact from Context
- [ ] Navigation after editing
- [ ] Success messages

### Step 8: Navbar and 404
- [ ] Navbar with links and counter
- [ ] 404 page for unknown routes

### Step 9: Styling
- [ ] Basic CSS so it looks professional
- [ ] Responsive (optional)

### Step 10: Extras (Optional)
- [ ] Persistence with localStorage
- [ ] Search/filter contacts
- [ ] Sort alphabetically
- [ ] Validate duplicate phone numbers

---

## 🎯 Evaluation Criteria

Your project will be evaluated on:

### Functionality (40%)
- ✅ Full CRUD works correctly
- ✅ Navigation between pages
- ✅ Forms with validations
- ✅ Shared global state

### Code (30%)
- ✅ Correct use of useReducer + Context
- ✅ Router configured correctly
- ✅ Well-organized components
- ✅ Clean, commented code

### UX/UI (20%)
- ✅ Friendly, intuitive interface
- ✅ Success/error messages
- ✅ Confirmations before deleting
- ✅ Clear validations

### Extras (10%)
- ✅ Persistence with localStorage
- ✅ Responsive design
- ✅ Additional features

---

## 🔗 Resources and References

### Official Documentation
- [React Router v6 - Tutorial](https://reactrouter.com/en/main/start/tutorial)
- [useReducer + Context](https://react.dev/learn/scaling-up-with-reducer-and-context)
- [Forms in React](https://react.dev/reference/react-dom/components/input)

### 4Geeks Academy — Official Project
- [Contact List App Using React & Context](https://4geeks.com/project/contact-list-context)

### Review the Previous Steps
- **Step 1-4**: React Router
- **Step 5-6**: useReducer
- **Step 7**: Context API
- **Step 8**: useReducer + Context
- **Step 9**: Router + Context integration

---

## 💡 Implementation Tips

### 1. Start Simple
Don't try to do everything at once. Build step by step:
1. Basic setup
2. Context working
3. One route (list)
4. Second route (add)
5. And so on

### 2. Test Frequently
After each feature, test that it works before moving on.

### 3. Use console.log
To debug the state and the actions being dispatched.

### 4. Keep Validations Simple at First
Start with basic validations (non-empty fields), then improve.

### 5. Style at the End
First make it work, then make it look good.

---

## 🆘 Need Help?

### If You're Stuck:
1. **Review the previous steps** — especially 7, 8, and 9
2. **Read the error in the console** — it tells you exactly what's missing
3. **Break down the problem** — if something doesn't work, simplify it
4. **Ask on Slack** — share the specific error
5. **Check the official documentation** — React Router and React Docs

### Common Mistakes:
- ❌ Forgetting to wrap with Providers
- ❌ Trying to use useNavigate outside BrowserRouter
- ❌ Mutating state in the reducer
- ❌ Not validating that the contact exists before showing it
- ❌ Forgetting `replace` in Navigate

---

## 📦 Submission

### What to Submit?
- GitHub repository with the code
- README.md with instructions to run the project
- (Optional) Deploy on Netlify/Vercel

### Instructions in the README:
```markdown
# Contact List App

Contact management application with React Router and Context API.

## Installation
\`\`\`bash
npm install
\`\`\`

## Run
\`\`\`bash
npm run dev
\`\`\`

## Technologies
- React 18
- React Router v6
- Context API + useReducer
- Vite
```

---

## ✅ Summary

### You Have Learned:
- ✅ Navigation with React Router
- ✅ Complex state with useReducer
- ✅ Global state with the Context API
- ✅ The Store pattern (useReducer + Context)
- ✅ Router + Context integration

### Now You Can:
- ✅ Build multi-page applications
- ✅ Manage complex global state
- ✅ Build complete CRUDs
- ✅ Apply professional React patterns

---

**Get to work! 🚀 This project shows you've mastered React at a professional level.**

**Remember**: There's no solved version. **YOU** are the one building this project by applying everything you've learned. Trust yourself!

---

**Made with ❤️ for 4Geeks Academy - Cohort España FS PT 129**
