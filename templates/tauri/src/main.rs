#![cfg_attr(
all(not(debug_assertions), target_os = "windows"),
windows_subsystem = "windows"
)]

mod lib;

#[tauri::command]
fn tauri_command() {
    let _ = lib::print_hello();
}

fn main() -> Result<(),()> {
    let context = tauri::generate_context!();
    tauri::Builder::default()
        .menu(tauri::Menu::os_default(&context.package_info().name))
        .invoke_handler(tauri::generate_handler![tauri_command])
        .run(context)
        .expect("error while running tauri application");
    Ok(())
}
