fn main () -> Result<(),std::io::Error> {
    let _ = mdbook_to_example::Builder::new()
        .set_name("${{NAME}}-book")
        .run();
    Ok(())
}
