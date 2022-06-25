rd /s /q crystal_engine
mkdir crystal_engine
git clone https://github.com/mikael-chowdhury/crystal-engine.git
robocopy ./crystal-engine/src/crystal_engine ./crystal_engine /E
rd /s /q crystal-engine
rmdir crystal-engine