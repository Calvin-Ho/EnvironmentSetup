This branch stores files for setting up an ***office*** Linux environment.  For a home setup, see the 'home' branch.

The various Vim plugins are stored as submodules.  When you first clone this repository, you will need to issue the following commands:

`git submodule init`

`git submodule update [--recursive]`

Alternatively, you can choose to clone specific submodules.  You can view all submodules inside the .gitmodules file directly or you can use this command:

`git config --file .gitmodules --get-regexp path | awk '{ print $2 }'`

Then, you can init and update a specific submodule with:

`git submodule update --init -- <path_to_submodule>`
