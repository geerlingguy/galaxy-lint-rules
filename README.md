galaxy-lint-rules
=================

This repository contains custom [Ansible Lint rules](https://github.com/willthames/ansible-lint) that will be used by [the Galaxy server](https://galaxy.ansible.com), starting in version 3.1 (under development), and a yet to be determined future release of [Mazer, the new Galaxy CLI](https://github.com/ansible/mazer), to evaluate Ansible content. Initially started with ansible-lint rules from [ansible-lint](https://github.com/willthames/ansible-lint), [ansible-review](https://github.com/willthames/ansible-review), and [tsukinowasha/ansible-lint-rules](https://github.com/tsukinowasha/ansible-lint-rules).

Rules
-----

| id                                                          | sample message                                              |
|-------------------------------------------------------------|-------------------------------------------------------------|
| **E1**                                                      | *deprecated*                                                |
| E101                                                        | Deprecated sudo                                             |
| E102                                                        | Using bare variables is deprecated                          |
| E103                                                        | Deprecated always_run                                       |
| E104                                                        | No Jinja2 in when                                           |
| E105                                                        | Deprecated module                                           |
| E106                                                        | Deprecated with_X for loops                                 |
|                                                             |                                                             |
| **E2**                                                      | *formatting*                                                |
| E201                                                        | Trailing whitespace                                         |
| E202                                                        | Variables should have spaces after {{ and before }}         |
| E203                                                        | Most files should not contain tabs                          |
| E204                                                        | Lines should be no longer than 100 chars                    |
| E205                                                        | Variables should be enclosed by spaces "{{ foo }}"          |
| E206                                                        | Use ":" YAML format when arguments are over 4               |
| E207                                                        | Playbooks should have the ".yml" extension                  |
|                                                             |                                                             |
| **E3**                                                      | *command-shell*                                             |
| E301                                                        | Using command rather than module                            |
| E302                                                        | Using command rather than an argument to e.g. file          |
| E303                                                        | Commands should not change things if nothing needs doing    |
| E304                                                        | Use shell only when shell functionality is required         |
| E305                                                        | Environment variables don't work as part of command         |
| E306                                                        | Use patch module                                            |
|                                                             |                                                             |
| **E4**                                                      | *module*                                                    |
| E401                                                        | Git checkouts must contain explicit version                 |
| E402                                                        | Mercurial checkouts must contain explicit revision          |
| E403                                                        | Octal file permissions must contain leading zero            |
| E404                                                        | Package installs should not use latest                      |
| E405                                                        | Doesn't need a relative path in role                        |
| E406                                                        | Template files should have the extension '.j2'              |
| E407                                                        | Recommended to mention the state                            |
|                                                             |                                                             |
| **E5**                                                      | *task*                                                      |
| E501                                                        | All tasks should be named                                   |
| E502                                                        | become_user requires become to work as expected             |
| E503                                                        | Tasks that run when changed should likely be handlers       |
| E504                                                        | Do not use local_action. use delegate_to: localhost instead |
|                                                             |                                                             |
| **E6**                                                      | *idiom*                                                     |
| E601                                                        | Don't compare to literal True/False                         |
| E602                                                        | Don't compare to empty string                               |