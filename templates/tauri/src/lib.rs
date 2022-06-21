/// Prints hello
///
/// ```
/// fn main() -> Result<(),()> {
///     ${{NAME}}::print_hello();
///     Ok(())
/// }
/// ```
pub fn print_hello() -> Result<(),()> {
    println!("Hello World!");
    Ok(())
}
