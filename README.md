<div align="center">

# Please wait until the template workflow finishes

Once it's finished you'll have to refresh the page
</div>

## Templates

The description of the repository you create is used as arguments for the project creator.

The first argument is which template to use, all other arguments depend on which template is being used since different templates may use different arguments. The owner and repository names are supplied to the template automatically.

**IMPORTANT:** You need to set your project to `Public` in order to use the description for arguments. If you set your project to Private the "none" template will be used. You can change the visibility of the project to Private after the initial workflow has been run, it just has to be public for the template creation process to be able to fetch the repo description.

### none

Creates a basic project reminiscent of what you would get from running `cargo init`. Also comes with a ready to go `book` folder which uses `mdbook`, and `examples` folder to get you started on that. All other templates follow the same basic layout as the "none" template, but with added extras.

```text
Whatever text you want
```

### tauri

Creates a basic Tauri project. Planned optional arguments include adding which flavor you want to use for your frontend, e.g. Vue, React or Svelte.

```text
tauri
```
