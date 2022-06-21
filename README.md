<div align="center">

# Please wait until the template workflow finishes

Once it's finished you'll have to refresh the page
</div>

## Templates

The description of the repository you create is used as arguments for the project creator.

The first argument is which template to use, all other arguments depend on which template is being used since different
templates may use different arguments. The owner and repository names are supplied to the template automatically.

**IMPORTANT:** You need to set your project to `Public` in order to use the description for arguments. If you set your
project to Private the "none" template will be used. You can change the visibility of the project to Private after the
initial workflow has been run, it just has to be public for the template creation process to be able to fetch the repo
description.

**IMPORTANT:** If your repository is created inside an organization, you can set an organization secret
called `WORKFLOW_TOKEN` with the contents of a PAT (personal access token) that has the `workflows` scope. That way the
template will automatically create the `.github` folder with a base set of workflows to perform common tasks. Personal
accounts and organizations without a `WORKFLOW_TOKEN` secret will have the `.github` directory renamed to `github` (
the `.` removed) so that all you have to do to get the base set of workflows running is check out the repository and
rename the folder.

### none

Creates a basic project reminiscent of what you would get from running `cargo init`. Also comes with a ready to
go `book` folder which uses `mdbook`, and `examples` folder to get you started on that. All other templates follow the
same basic layout as the "none" template, but with added extras.

```text
Whatever text you want
```

### tauri

Creates a basic Tauri project. Planned optional arguments include adding which flavor you want to use for your frontend,
e.g. Vue, React or Svelte.

```text
tauri
```
